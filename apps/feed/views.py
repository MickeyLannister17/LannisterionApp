from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Post

# Create your views here.


@login_required
def feed(request):
    
    userids = [request.user.id]
    
    for lannisterian in request.user.lannisterianprofile.follows.all():
        userids.append(lannisterian.user.id)
        
    posts =Post.objects.filter(created_by_id__in=userids)    

    return render(request, 'feed/feed.html', {'posts': posts})

@login_required
def search(request):
    query = request.GET.get('query', '')
    
    if len(query) > 0:
        lannisterians = User.objects.filter(username__icontains=query)
        
    else:
        lannisterians = []
        
    context = {
        'query' : query,
        'lannisterians' : lannisterians
    }   
    
    return render(request, 'feed/search.html', context) 