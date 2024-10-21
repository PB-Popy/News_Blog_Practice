from django.shortcuts import render,redirect

from myApp.models import *
from myBlogApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def signupPage(request):
    
    if request.method=='POST':
        
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        Confirm_password=request.POST.get("Confirm_password")
        user_type=request.POST.get("user_type")
    
        
        if password==Confirm_password:
            
            
            user=customUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                user_type=user_type,
               
            )
            
            if user_type=='viewers':
                viewersProfileModel.objects.create(user=user)
                
            elif user_type=='creator':
                creatorProfileModel.objects.create(user=user)
            
            return redirect("signInPage")
            
    return render(request,"signupPage.html")


def signInPage(request):
    if request.method == 'POST':
        
        user_name=request.POST.get("username")
        pass_word=request.POST.get("password")

        try:
            user = authenticate(request, username=user_name, password=pass_word)

            if user is not None:
                login(request, user)
                return redirect('homePage') 
            else:
                return redirect('signInPage')

        except customUser.DoesNotExist:
            return redirect('signInPage')

    return render(request, 'signInPage.html')

@login_required
def homePage(request):
    
    
    return render(request,"homePage.html")


def logoutPage(request):
    
    logout(request)
    
    return redirect('signInPage')

@login_required
def profilePage(request):
    
    return render(request,"profilePage.html")

@login_required
def addNewsPage(request):

    current_user= request.user

    if request.method== 'POST':
        title= request.POST.get('title')
        content= request.POST.get('content')
        author= request.POST.get('author')
        categories= request.POST.get('categories')
        image= request.FILES.get('image')

        news=NewsPostModel(
            user=current_user,
            title=title,
            content=content,
            author=author,
            categories=categories,
            image=image,
        )
        news.save()

        return redirect('createdNewsPage')

    
    return render(request,"addNewsPage.html")


@login_required
def addBlogPage(request):

    current_user= request.user

    if request.method== 'POST':
        title= request.POST.get('title')
        content= request.POST.get('content')
        author= request.POST.get('author')
        categories= request.POST.get('categories')
        comments= request.POST.get('comments')
        image= request.FILES.get('image')

        blog=BlogManagementModel(
            user=current_user,
            title=title,
            content=content,
            author=author,
            categories=categories,
            comments=comments,
            image=image,
        )
        blog.save()

        return redirect('createdBlogPage')

    
    return render(request,"addBlogPage.html")

@login_required
def createdNewsPage(request):
    current_user=request.user

    news=NewsPostModel.objects.filter(user=current_user)

    context={
        'news':news
    }
    
    return render(request,"createdNewsPage.html",context)

@login_required
def createdBlogPage(request):
    current_user=request.user

    blog=BlogManagementModel.objects.filter(user=current_user)

    context={
        'blog':blog
    }
    
    return render(request,"createdBlogPage.html",context)


def deleteNews(request,news_id):

    news=NewsPostModel.objects.get(id=news_id)

    news.delete()

    return redirect('createdNewsPage')

def editNews(request,news_id):
    current_user=request.user

    news=NewsPostModel.objects.get(id=news_id)

    context={
        'news':news
    }

    if request.method== 'POST':
        news_id=request.POST.get('news_id')
        title= request.POST.get('title')
        content= request.POST.get('content')
        author= request.POST.get('author')
        categories= request.POST.get('categories')
        image= request.FILES.get('image')

        news=NewsPostModel(
            id=news_id,
            user=current_user,
            title=title,
            content=content,
            author=author,
            categories=categories,
            image=image,
        )
        news.save()

        return redirect('createdNewsPage')
    return render(request,'editNews.html',context)

def deleteBlog(request,blog_id):

    blog=BlogManagementModel.objects.get(id=blog_id)
    blog.delete()

    return redirect('createdBlogPage')


def editBlog(request,blog_id):
    current_user=request.user

    blog=BlogManagementModel.objects.get(id=blog_id)

    context={
        'blog':blog
    }

    if request.method== 'POST':
        blog_id=request.POST.get('blog_id')
        title= request.POST.get('title')
        content= request.POST.get('content')
        author= request.POST.get('author')
        categories= request.POST.get('categories')
        image= request.FILES.get('image')

        blog=BlogManagementModel(
            id=blog_id,
            user=current_user,
            title=title,
            content=content,
            author=author,
            categories=categories,
            image=image,
        )
        blog.save()

        return redirect('createdBlogPage')
    return render(request,'editBlog.html',context)

def allBlogPost(request):
    blog=BlogManagementModel.objects.all()
    news=NewsPostModel.objects.all()

    context={
        'blog':blog,
        'news':news
    }

    return render(request,'allBlogPost.html',context)