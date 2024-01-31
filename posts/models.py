from django.db import models
from datetime import datetime
from abstract.models import AbstractModel, AbstractManager
from ckeditor.fields import RichTextField

class PostManager(AbstractManager):
    pass

# Create your models here.

class Post(AbstractModel):
    image = models.ImageField(upload_to='jacsblog/uploaded')
    title = RichTextField()
    body =  RichTextField()
    created_at = models.DateTimeField(default = datetime.now, blank=True)

    objects = PostManager()
    