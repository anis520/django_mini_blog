from django.shortcuts import render

# Create your views here.
def planing_views(req):
    return render(req,'planing/planing.html')
    