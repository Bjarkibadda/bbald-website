from django.db import models
from tinymce.models import HTMLField # remember to delete tinyemc package.
from ckeditor.fields import RichTextField 
# RichTextField from django-ckeditor package - allow us to add image and style our posts.


# Create your models here.

class Post(models.Model):
    title =  models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    content = RichTextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add = True)
    header_pic = models.ImageField(null=True, upload_to='pictures')

    class Meta:
        ordering = ['timestamp'] 
        
    def __str__(self):
        return self.title
 