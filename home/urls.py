 
from django.urls import path
from .views import home,homeText,deletedata,editdata
urlpatterns = [
 
    path('',home ),
    path('addnewhome/',homeText,name='addhome'),
    path('delete/<int:id>',deletedata,name='delete'),
    path('edit/<int:id>',editdata,name='edit'),
 
]
