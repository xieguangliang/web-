from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_view_func(request):
    return HttpResponse('hello world')