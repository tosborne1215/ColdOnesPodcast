from django.db import models
from blog.models import Post

# Create your models here.
class Episode(Post):
    file_location = models.CharField(max_length=255)
