from django.contrib import admin

# Register your models here.

from main.models import Post, Category

admin.site.register(Category)
admin.site.register(Post)
