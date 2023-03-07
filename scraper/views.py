from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('Hello World!')
def csv(request):
    return HttpResponse('CSV')