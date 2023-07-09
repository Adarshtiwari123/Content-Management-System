from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import AdminLogin,Enquery,Blog
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout

# Create your views here.
#bussiness logic layer
def view_index(request):
    resp=render(request,"basic_app/index.html")
    return resp
def view_aboutus(request):
    resp=render(request,"basic_app/aboutus.html")
    return resp
def view_ourmission(request):
    resp=render(request,"basic_app/ourmission.html")
    return resp

def logoutUser(request):
    try:
            logout(request)
            messages.warning(request,"Successfully logout")

            """return  redirect(reverse('inherit'))"""
            return redirect("basic_app:view_index")
    except ObjectDoesNotExist:
        return render(request,"basic_app/admin_login.html")
    #  logout(request)
    #  return redirect("/")
   
        
def view_blog(request):
    blogs=Blog.objects.all()
    d={
        'blogs':blogs
    }
    resp=render(request,"basic_app/blog_index.html",context=d)
    return resp
def view_contactus(request):
    resp=render(request,"basic_app/contactus.html")
    return resp
def view_adminlogin(request):
    resp=render(request,"basic_app/admin_login.html")
    return resp
def admindashboard(request):
    resp=render(request,"basic_app/admindashboard.html")
    return resp
def validateuser(request):
     if request.method=="GET":
            resp=render(request,"basic_app/admin_login.html")
            return resp
     elif request.method=="POST":
      adminid=request.POST['email']
      password=request.POST['password']
     try:
       object=AdminLogin.objects.get(adminid=adminid,password=password)
       if object is not None:
           request.session['adminid']=adminid
           return render(request,"basic_app/admindashboard.html")
     except ObjectDoesNotExist:
        return render(request,'basic_app/admin_login.html')
def enqueryform(request):
    if request.method=="GET":
        return render(request,"basic_app/contactus.html")
    elif request.method=="POST":
        en=Enquery()
        en.username=request.POST.get('username',"NA")
        en.phone=int(request.POST.get('phonenumber',0))
        en.useremail=request.POST.get("useremail","NA")
        en.course=request.POST.get('course',"N/A")
        en.message=request.POST.get("message","NA")
        en.save()
        messages.success(request, "Thank you for ")
        return render(request,'basic_app/contactus.html')

def enquiry_show(request):
    data=Enquery.objects.all()
    d={'data':data}
    return render(request,"basic_app/enquiry_show.html",context=d)
def blogs(request):
    resp=render(request,"basic_app/blogs.html")
    return resp
def createblog(request):
    resp=render(request,"basic_app/blogs.html")
    return resp
def blog_create(request):
    if request.method=="GET":
        resp=render(request,"basic_app/blogs.html")
        return resp
    elif request.method=="POST":
        b=Blog()
        b.Title=request.POST.get('title',"N/A")
        b.category=request.POST.get('category',"N/A")
        b.image=request.POST.files=request.FILES.get("photo","N/A")
        b.description=request.POST.get("description","N/A")
        b.save()
        resp=HttpResponse("<h1>Thanks for creation</h1>")
        return resp
