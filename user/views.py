from django.http import HttpResponse
from django.shortcuts import render

def user_page(request):
    return render(request, 'user/user_personal_cabinet_page.html')
