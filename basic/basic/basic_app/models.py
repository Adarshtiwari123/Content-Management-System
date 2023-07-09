from django.db import models

# Create your models here.
class AdminLogin(models.Model):
    adminid = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=20)
class Enquery(models.Model):
    username=models.CharField(max_length=20)
    phone=models.IntegerField()
    useremail=models.EmailField(max_length=30,blank=False)
    course=models.CharField(max_length=20)
    message=models.TextField(max_length=100)

class Blog(models.Model):
    Title=models.CharField(max_length=50,blank=False)
    category=models.CharField(max_length=20)
    image=models.ImageField()
    description=models.TextField(max_length=200)
    # blogdate=models.DateField(max_length=10,auto_created=True)