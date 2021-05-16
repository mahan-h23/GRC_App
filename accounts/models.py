from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models

from django.contrib.auth.models import Group ,User



class ProfileInfo(models.Model):
    username = models.OneToOneField(AUTH_USER_MODEL,related_name='user_profile',on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    position = models.ForeignKey(Group,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.name







