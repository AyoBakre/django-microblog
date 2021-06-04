from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Hii Bruverly')


def about(request):
    return HttpResponse('wanna know about me?')
