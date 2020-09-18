from django.contrib import admin

# Register your models here.

from .models import Post

class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ("js/blog.js",)

admin.site.register(Post, PostAdmin)