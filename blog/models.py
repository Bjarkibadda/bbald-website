from django.db import models
from tinymce.models import HTMLField # remember to delete tinyemc package.
from ckeditor.fields import RichTextField 
import datetime
# RichTextField from django-ckeditor package - allow us to add image and style our posts.

month_list = [
    ''
]

# Create your models here.

class Post(models.Model):
    title =  models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    content = RichTextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add = True)
    header_pic = models.ImageField(null=True, upload_to='pictures')
    prj_or_blog = models.BooleanField(default=False)
    extract = models.CharField(max_length=300, default="Extract from post")

    class Meta:
        ordering = ['timestamp'] 
        
    def __str__(self):
        return self.title

    def get_date(self):
        new_format = str(self.timestamp).split(' ')
        year, month, date = new_format[0].split('-')
        month = datetime.datetime.strptime(month, "%m")
        month_name = month.strftime("%B")
        return "{} - {} - {}".format(date, month_name, year)
        
 