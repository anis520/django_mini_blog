from django.shortcuts import render

# Create your views here.
def buniness_views(req):
    return render(req,'business/business.html')