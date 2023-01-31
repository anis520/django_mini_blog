from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .models import Homepost
from .forms import Homeadd
from django.contrib import messages


# Create your views here.
def home(req):
    data=Homepost.objects.all()

    return render(req,'home/home.html',{'data':data})



   # add home text views 

def homeText(req):
    
    if req.user.is_authenticated: 
      if req.method=='POST':
          form=Homeadd(req.POST)
          if form.is_valid():
            title=form.cleaned_data['title']
            text=form.cleaned_data['text']
            data=Homepost(title=title,text=text)
            data.save()
            messages.success(req,'Data insert successfully')
            return HttpResponseRedirect('/userprofile/')
      else:      
        fm=Homeadd()
        return render(req,'home/addnew.html',{'form':fm})
    else:
        messages.warning(req,'your are not authoriged')
        return HttpResponseRedirect('/login')
    




def deletedata(req,id):
 if req.user.is_authenticated: 
   data=Homepost.objects.get(id=id)
   data.delete()   
   return HttpResponseRedirect('/userprofile')
 else:
   messages.warning(req,'your are not authoriged')
   return HttpResponseRedirect('/login')
    



# edit data 

def editdata(req,id):
 if req.user.is_authenticated:      
  if req.POST:
    pi=Homepost.objects.get(pk=id)
    data=Homeadd(req.POST,instance=pi)
    if data.is_valid():
       data.save()
       messages.success(req,'Update successfully')
       return HttpResponseRedirect('/userprofile')    
  else:
    data=Homepost.objects.get(pk=id)
    pi=Homeadd(instance=data)
  return render(req,'home/addnew.html',{'form':pi})
 
 else:
   messages.warning(req,'your are not authoriged')
   return HttpResponseRedirect('/login')
    
