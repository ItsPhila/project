from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import CommentForm, AddPost

def index(request):
  
    all_post = Post.objects.order_by('-pubdate')
    context = {"all_post" : all_post}
    return render(request,'main/index.html',context)
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
    return render(request,'main/addnew.html',context)

def detail(request,blog_id):
    single_post = Post.objects.get(id=blog_id)
    comments = single_post.comment_set.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = single_post
            form.save()
            form = CommentForm()

    else:
        form = CommentForm()  
    context = {"single_post" : single_post, "comments": comments, "form":form}
    return render(request,'main/detail.html',context)