from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<marquee scrollamount=""scrolldelay=""direction=""behavior=""loop="">This is our first view function</marquee>')