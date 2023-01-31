from django.shortcuts import render,HttpResponseRedirect
from .forms import Login_form
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def login_view(req):
    if not req.user.is_authenticated:  
       if req.method=='POST':
         form =Login_form(request=req,data=req.POST)
         if form.is_valid():
          uname=form.cleaned_data['username']    
          upass=form.cleaned_data['password'] 
          getdata= authenticate(username=uname,password=upass)
          if getdata is not None:
                login(req,getdata)
                messages.success(req,f'hello {uname} Welcome to profile')
                return HttpResponseRedirect('/userprofile/')  
       else:     
         form=Login_form()
       return render(req,'login/login.html',{'form':form})
    else:
       messages.success(req, ' you are already loging')
       return HttpResponseRedirect('/userprofile/') 



# logout view 
def logout_view(req):
    logout(req)
    return HttpResponseRedirect('/login')
