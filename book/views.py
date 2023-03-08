from django.http import HttpResponse
from django.shortcuts import render

def books_page(request):
    return HttpResponse('Books')
