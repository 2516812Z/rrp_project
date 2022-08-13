from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User

class Users(models.Model):
    MAX_PASSWORD_LENGTH = 30
    MAX_USERNAME_LENGTH = 30

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    class Meta:
        app_label = 'rrp'

    def __str__(self):
        return self.user.username








