from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=10000)
    pub_date = models.DateTimeField()
