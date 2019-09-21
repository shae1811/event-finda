from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=30)
  
  
  def __str__(self):
    return self.email

# Create your models here.
