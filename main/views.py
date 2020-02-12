from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
# from django.shortcuts import (
# render_to_response
# )
from django.template import RequestContext


class IndexView(TemplateView):
    name = 'main'
    template_name = 'main/index.html'

def home(request):
    return render(request,'main/index.html')

# HTTP Error 404
def page_not_found(request, exception):
    return render(request,'main/404.html',)
# HTTP Error 500
def server_error(request):
    return render(request,'main/500.html',)
