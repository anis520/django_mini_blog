from django.urls import path
from .views import userprofile_views


urlpatterns = [
    path('userprofile/',userprofile_views,name='profile'),
    
    
    ]
