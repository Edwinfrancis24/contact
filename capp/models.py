from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=100)
    contact_phone = models.CharField(max_length=20)