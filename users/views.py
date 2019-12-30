from django.shortcuts import render, redirect  
from .forms import SignUpFrom

def register(request): 
    if request.method == 'POST':
        form = SignUpFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:index')

    else:
        form = SignUpFrom()
    return render(request, 'main/register.html', {'form':form})
