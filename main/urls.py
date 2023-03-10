from django.urls import path

from main import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
    path('about', views.AboutPage.as_view(), name='about_page'),
    path('contacts', views.ContacsPage.as_view(), name='contacts')
]