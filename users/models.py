from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    #Proxy model that extends the User model from django.contrib.auth.models with additional information
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        #Return username in console when queries are done
        return self.user.username