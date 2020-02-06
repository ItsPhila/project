from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import AddPost
from django.contrib.auth.decorators import login_required, user_passes_test


def index(request):
  
    all_post = Post.objects.order_by('-pubdate')
    context = {"all_post" : all_post}
    return render(request,'post/index.html',context)

# @user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/registration/login/')
def addpost(request):
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.reporter = request.user
            form.save()
            form = AddPost()

    else:
        form = AddPost()  
    context = {"form":form}
    return render(request,'post/addnew.html',context)

def detail(request,post_id):
    single_post = Post.objects.get(id=post_id)
    context = {"single_post" : single_post,}
    return render(request,'post/detail.html',context)
