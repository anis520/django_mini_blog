from django.contrib import admin

# Register your models here.
from .models import Homepost

@admin.register(Homepost)
class HomePostAdmin(admin.ModelAdmin):
    list_display=['id','title','text']