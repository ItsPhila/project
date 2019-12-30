from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    name = 'main'
    template_name = 'main/index.html'

def home(request):
    return render(request,'main/index.html')