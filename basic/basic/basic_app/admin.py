from django.contrib import admin
from . models import AdminLogin,Enquery,Blog
# Register your models here.
admin.site.register(AdminLogin)
admin.site.register(Enquery)
admin.site.register(Blog)