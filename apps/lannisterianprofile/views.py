from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import LannisterianProfileForm
from apps.notification.utilities import create_notification
# Create your views here.

def lannisterianprofile(request, username):
    user = get_object_or_404(User, username=username)
    posts = user.posts.all()

    for post in posts:
        likes = post.likes.filter(created_by_id=request.user.id)

        if likes.count() > 0:
            post.liked = True
        else:
            post.liked = False

    context = {
        'user': user,
        'posts': posts
    }   
    return render(request, 'lannisterianprofile/lannisterianprofile.html', context)

print('working!')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form =  LannisterianProfileForm(request.POST, request.FILES, instance=request.user.lannisterianprofile)

        if form.is_valid():
            form.save()

            return redirect('lannisterianprofile', username=request.user.username)
    else:
        form = LannisterianProfileForm(instance=request.user.lannisterianprofile)
    
    context = {
        'user': request.user,
        'form': form
    }

    return render(request, 'lannisterianprofile/edit_profile.html', context)


@login_required
def follow_lannisterian(request, username):
    user = get_object_or_404(User, username=username)
    
    request.user.lannisterianprofile.follows.add(user.lannisterianprofile)
    
    create_notification(request, user, 'follower')
    return redirect('lannisterianprofile', username=username)

@login_required
def unfollow_lannisterian(request, username):
    user = get_object_or_404(User, username=username)
    
    request.user.lannisterianprofile.follows.remove(user.lannisterianprofile)
    
    return redirect('lannisterianprofile', username=username)

def followers(request, username):
    user = get_object_or_404(User, username=username)
    
    return render(request, 'lannisterianprofile/followers.html', {'user': user})

def follows(request, username):
    user = get_object_or_404(User, username=username)
    
    return render(request, 'lannisterianprofile/follows.html', {'user': user})