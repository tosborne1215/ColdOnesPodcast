from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
