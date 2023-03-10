from django.http import HttpResponse
from django.shortcuts import render

def books_page(request):
    return render(request, 'book/book_list_page.html')
