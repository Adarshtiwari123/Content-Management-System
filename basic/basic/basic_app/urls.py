from  django.urls import path
from .views import *
from basic_app import views
app_name = "basic_app"
urlpatterns = [
    path('',views.view_index,name="view_index"),
    path('about/',views.view_aboutus,name="view_aboutus"),
    path('blog/',views.view_blog,name="view_blog"),
    path('mission/',views.view_ourmission,name="view_ourmission"),
    path('contact/',views.view_contactus,name="view_contactus"),
    path('adminlogin/',views.view_adminlogin,name="view_adminlogin"),
    path('validate/',views.validateuser,name="validateuser"),
    path('dashboard/',views.admindashboard,name="admindashboard"),
    path('enqueryform/',views.enqueryform,name="enqueryform"),
    path('enquiry_show/',views.enquiry_show,name="enquiry_show"),
    path('blogs/',views.blogs,name="blogs"),
    path('createblog/',views.createblog,name="createblog"),
    path('blog_create/',views.blog_create,name="blog_create"),
    path("logoutUser/",views.logoutUser,name="logoutUser"),
    
    
]
