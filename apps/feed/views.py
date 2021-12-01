from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from apps.notification.utilities import create_notification

from .models import Post

# Create your views here.


@login_required
def feed(request):
    
    userids = [request.user.id]
    
    for lannisterian in request.user.lannisterianprofile.follows.all():
        userids.append(lannisterian.user.id)
        
    posts =Post.objects.filter(created_by_id__in=userids)
    
    for post in posts:
        likes = post.likes.filter(created_by_id=request.user.id)
        
        if likes.count() > 0:
            post.liked = True
            
        else:
            post.liked = False       

    return render(request, 'feed/feed.html', {'posts': posts})

@login_required
def search(request):
    query = request.GET.get('query', '')
    
    if len(query) > 0:
        lannisterians = User.objects.filter(username__icontains=query)
        posts = Post.objects.filter(body__icontains=query)
        
    else:
        lannisterians = []
        posts = []
        
    context = {
        'query' : query,
        'lannisterians' : lannisterians,
        'posts' : posts
    }   
    
    return render(request, 'feed/search.html', context) 