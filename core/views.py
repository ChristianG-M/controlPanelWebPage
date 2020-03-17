from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your vistas basadas en clase.
class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':'Mi Super Web Get Method'})

# Create your views here.