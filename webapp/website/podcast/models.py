from django.db import models
from blog.models import Post
from .episode_upload import S3StorageWrapper

# Create your models here.


class Episode(Post):
    file_location = models.CharField(max_length=255)
    episode_file = models.FileField(storage=S3StorageWrapper())
