from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.
def index(request):
    
    return render(request, "home.html",{
        'posts': Post.objects.all
    })

def blogpost(request, id):
    return render(request, "blogpost.html",{
        'post': Post.objects.get(id = id),
        'form': CommentForm
        
    })