import json
import re
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from apps.notification.utilities import create_notification
from django.contrib.auth.models import User

from .models import Like, Post

@login_required
def api_add_post(request):
    data = json.loads(request.body)
    body = data['body']
    
    post = Post.objects.create(body=body, created_by=request.user)
    
    results = re.findall("(^|[^@\w])@(\w{1,20})")
    
    for result in results:
        result = result[1]
        
        print (result)
        
        if User.objects.filter(username=result).exists() and result != request.user.username:
            create_notification(request, User.objects.get(username=result), 'mention')
    
    return JsonResponse({'success' : True})

# @login_required
# def api_like_post(request):
#     data = json.loads(request.body)
#     body = data['post_id']
    
#     if not Like.objects.filter(post_id=post_id).filter(created_by=request.user).exists():
#         like = Like.objects.created(post_id=post_id, created_by=request.user)
        
#     json_response = {'success': True}

@login_required
def api_like_post(request):
    data = json.loads(request.body)
    post_id = data['post_id']

    if not Like.objects.filter(post_id=post_id).filter(created_by=request.user).exists():
        like = Like.objects.create(post_id=post_id, created_by=request.user)
        post = Post.objects.get(pk=post_id)
        create_notification(request, post.created_by, 'like')
            
    return JsonResponse({'success': True})
    
    #return JsonResponse(json_response)    