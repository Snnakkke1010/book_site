from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):

    template_name = 'main/home_page.html'


class AboutPage(TemplateView):

    template_name = 'main/about_page.html'


class ContacsPage(TemplateView):

    template_name = 'main/contacts_page.html'
