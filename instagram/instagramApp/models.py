from django.db import models
from django.utils import timezone

# Create your models here.
class Post (models.Model):
    author = models.ForeignKey('author.User',on_delete=models.CASCADE)
    image = models.ImageField(blank=True,null=True)
    caption=models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
