from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    phonenum = models.CharField(max_length=10,unique=True,null=True)