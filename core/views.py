from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your vistas basadas en clase.
class HomePageView(TemplateView):
    template_name = "core/home.html"

# Create your views here.