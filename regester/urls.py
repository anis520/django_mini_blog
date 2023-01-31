from django.urls import path
from .views import regester_veiw

urlpatterns = [
    
   path('regester/',regester_veiw,name='regester')


]
