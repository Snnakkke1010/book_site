from django.http import HttpResponse
from django.shortcuts import render

def user_page(request):
    return HttpResponse('User')
