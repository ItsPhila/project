from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Places
from .forms import AddPlace

def index(request):
      
    all_places = Places.objects.order_by('-pubdate')
    context = {"all_places" : all_places}
    return render(request,'places/index.html',context)

