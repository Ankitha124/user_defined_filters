from django.shortcuts import render

# Create your views here.

def usdf(request):
    d={'data':'HEllO jspiDErs'}

    return render(request,'usdf.html',d)

