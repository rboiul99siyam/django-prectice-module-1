from django.http import HttpResponse
from django.shortcuts import render

def home(res):
    return render(res ,'index.html')