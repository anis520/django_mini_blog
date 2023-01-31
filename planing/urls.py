from django.urls import path
from .views import planing_views

urlpatterns = [
    path('future/',planing_views,name='future')
]
