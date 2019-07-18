from django.contrib import admin
from .models import signupform,loginform,checkinform
# Register your models here.
from.models import  Signup
class  SignupAdmin (admin.ModelAdmin):
    list_display=['Platinum','suit','gold','ordinary']
Admin.site.Signup( Signup, SignupAdmin)
