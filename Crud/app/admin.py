from django.contrib import admin
from .models import StuReg

# Register your models here.
@admin.register(StuReg)
class StuRegAdmin(admin.ModelAdmin):
    list_display=('id','name','email','password')