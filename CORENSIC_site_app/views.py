from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from datetime import datetime


class HomePage(TemplateView):
    template_name = 'homepage.html'

    def get(self, request, *args, **kwargs):
        print(f"In function get: {datetime.now()}")
        return render(request, template_name='homepage.html')

    def post(self, request, *args, **kwargs):
        return render(request, template_name='homepage.html')
