from django.contrib import admin
from .models import Post

# class postsAdmin(admin.ModelAdmin):
#     readonly_fields = (id)

# Register your models here.
admin.site.register(Post)