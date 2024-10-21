from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from myProject.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',signupPage,name="signupPage"),
    path("signInPage/", signInPage, name="signInPage"),
    path("homePage/", homePage, name="homePage"),
    path("logoutPage/", logoutPage, name="logoutPage"),
    path("ProfilePage/", profilePage, name="profilePage"),

    path("addNewsPage/", addNewsPage, name="addNewsPage"),
    path("createdNewsPage/", createdNewsPage, name="createdNewsPage"),
    path("addBlogPage/", addBlogPage, name="addBlogPage"),
    path("createdBlogPage/", createdBlogPage, name="createdBlogPage"),

    path("editNews/<str:news_id>", editNews, name="editNews"),
    path("deleteNews/<str:news_id>", deleteNews, name="deleteNews"),
    path("editBlog/<str:news_id>", editBlog, name="editBlog"),
    path("deleteBlog/<str:news_id>", deleteBlog, name="deleteBlog"),
    
    path("allBlogPost", allBlogPost, name="allBlogPost"),

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)