from django.shortcuts import render
from SpeedApp.admin import *
def index_view(request):
    content={
        "title":"Sio",
        "tita":"Sia",
        "list":Article.objects.all()
    }

    return render(request,"index.html",content)

# Create your views here.
