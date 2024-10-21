from django.db import models
from django.contrib.auth.models import AbstractUser

class customUser(AbstractUser):
    
    USER=[
        ('viewers','Viewers'),
        ('creator','Creator'),
    ]
    user_type=models.CharField(choices=USER,max_length=100,null=True)
    
    
    def __str__(self):  
        
        return f"{self.username}"
    
class viewersProfileModel(models.Model):
    
    INTEREST=[
        ('desserts','Desserts'),
        ('vegan_recipes','VeganRecipes'),
    ]
    user=models.OneToOneField(customUser,on_delete=models.CASCADE,related_name='viewersProfile')
    Specialties = models.CharField(max_length=200, blank=True, null=True)
    Followers = models.PositiveIntegerField(blank=True, null=True)
    Achievements = models.CharField(max_length=200, blank=True, null=True)
    Interest = models.CharField(max_length=200, blank=True, null=True)
    Bio = models.TextField(max_length=200, blank=True, null=True)
    Profile_Pic = models.ImageField(upload_to='Media/Profile_Pic', blank=True, null=True)
   
    
    def __str__(self):
        return f"{self.user.username}"
    
    
class creatorProfileModel(models.Model):
    
    user = models.OneToOneField(customUser, on_delete=models.CASCADE,related_name='creatorsProfile')
    Specialties = models.CharField(max_length=200, blank=True, null=True)
    Followers = models.PositiveIntegerField(blank=True, null=True)
    Achievements = models.CharField(max_length=200, blank=True, null=True)
    Bio = models.TextField(max_length=200, blank=True, null=True)
    Profile_Pic = models.ImageField(upload_to='Media/Profile_Pic', blank=True, null=True)
   
    def __str__(self):
        return f"{self.user.username}"
    
  

class NewsPostModel(models.Model):

    CATEGORIES= [
        ('politics','Politics'),
        ('health','Health'),
        ('entertainment','Entertainment'),
        ('business','Business'),
        ('education','Education'),
    ]

    user = models.OneToOneField(customUser, on_delete=models.CASCADE,related_name='NewsPost')
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True)
    categories = models.CharField(choices=CATEGORIES, max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='Media/image', blank=True, null=True)

    def __str__(self):
        return self.title
    
