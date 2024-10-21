from django.db import models
from myApp.models import *

class BlogManagementModel(models.Model):

    CATEGORIES= [
        ('politics','Politics'),
        ('health','Health'),
        ('entertainment','Entertainment'),
        ('business','Business'),
        ('education','Education'),
    ]

    user = models.OneToOneField(customUser, on_delete=models.CASCADE,related_name='Blog_Management')
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True)
    categories = models.CharField(choices=CATEGORIES, max_length=200, blank=True, null=True)
    comments = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='Media/image', blank=True, null=True)

    def __str__(self):
        return self.title
