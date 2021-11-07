from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def lannisterianprofile(request, username):
   user = get_object_or_404(User, username=username)
   
   context = {
       'user' : user
   }
   
   return render(request, 'lannisterianprofile/lannisterianprofile.html', context)

print('working!')

@login_required
def follow_lannisterian(request, username):
    user = get_object_or_404(User, username=username)
    
    request.user.lannisterianprofile.follows.add(user.lannisterianprofile)
    
    return redirect('lannisterianprofile', username=username)

@login_required
def unfollow_lannisterian(request, username):
    user = get_object_or_404(User, username=username)
    
    request.user.lannisterianprofile.follows.remove(user.lannisterianprofile)
    
    return redirect('lannisterianprofile', username=username)

def followers(request, username):
    user = get_object_or_404(User, username=username)
    
    return render(request, 'lannisterianprofile/follows.html', {'user': user})