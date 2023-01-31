from django.urls import path
from .views import about_views


urlpatterns = [
    
   path('about/',about_views ,name='about')


]
