from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegesterForm
from django.contrib.auth.models import Group



# Create your views here.
def regester_veiw(req):
 if not req.user.is_authenticated:  
 
    if req.method=="POST":
     fm=RegesterForm(req.POST)
     name=req.POST['username']
     print(name)
     if fm.is_valid():
        if name=='anisahad':
         messages.warning(req,'this name is not allowed')
         return HttpResponseRedirect('/regester')

        else:
         messages.success(req,'congratulation your singup successfully !')
         user= fm.save()
         group=Group.objects.get(name='homeside')
         user.groups.add(group)
         return HttpResponseRedirect('/login')
    else:  
     fm=RegesterForm()
    return render(req,'regester/regester.html',{'form':fm})
 else:
    messages.success(req, 'Please logout frist for new singing')
    return HttpResponseRedirect('/userprofile/') 

 