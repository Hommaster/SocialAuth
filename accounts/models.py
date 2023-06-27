from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(blank=True, upload_to='photo/%Y/%m/%d')

    def __str__(self):
        return self.user.username
