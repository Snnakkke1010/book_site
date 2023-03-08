from django.urls import path

from user import views

urlpatterns = [
    path('', views.user_page, name='user_page')
]