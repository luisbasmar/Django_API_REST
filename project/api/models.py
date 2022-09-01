from django.db import models
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=80)
    user_name = models.CharField(max_length=80)
    email = models.CharField(max_length=80)