from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from home.models import Homepost
from django.contrib.auth.models import Group


# Create your views here.
def userprofile_views(req):
   if  req.user.is_authenticated: 
    groupdata=Group.objects.all()
    data=Homepost.objects.all()
    return render(req,'userprofile/userprofile.html',{'data':data,'gdata':groupdata})
   else:
     messages.warning(req,'Please loging first !!')   
     return HttpResponseRedirect('/login')
   


