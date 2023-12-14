from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to='jacsblog/uploaded')
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=10000000)
    created_at = models.DateTimeField(default = datetime.now, blank=True)

# class Like(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)