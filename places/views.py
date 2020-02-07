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

@login_required(redirect_field_name='/login/')
def addplace(request):
    if request.method == 'POST':
        form = AddPlace(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            form = AddPlace()
            return redirect('Places:index')

    else:
        form = AddPlace()  
    context = {"form":form}
    return render(request,'places/addplace.html',context)

