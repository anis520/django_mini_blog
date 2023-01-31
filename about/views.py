from django.shortcuts import render

# Create your views here.
def about_views(req):
    return render(req,'about/about.html')