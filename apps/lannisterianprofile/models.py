from django.contrib.auth.models import User
from django.db import models



# Create your models here.

class LannisterianProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
    
User.lannisterianprofile = property(lambda u:LannisterianProfile.objects.get_or_create(user=u)[0])