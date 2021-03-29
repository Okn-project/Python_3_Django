from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse ('<h1>first session</h1>')

def index(request):
    return render(request,'index.html')