from django.urls import path
from .views import buniness_views


urlpatterns = [
     
     path('business/',buniness_views,name='business')

]
