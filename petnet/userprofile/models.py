from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username