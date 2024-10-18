from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse


def frontpage(request):
    return render(request,"frontpage.html")