from django.urls import path

from book import views

urlpatterns = [
    path('', views.books_page, name='books_page')
]