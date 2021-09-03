from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    mypost = post.objects.all()
    context = {'lokeshpost':mypost}
    return render(request,'lokesh/index.html',context)
