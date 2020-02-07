from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Post
from .forms import AddPost



def index(request):
  
    all_post = Post.objects.order_by('-pubdate')
    context = {"all_post" : all_post}
    return render(request,'post/index.html',context)

# @user_passes_test(lambda u: u.is_superuser)
@login_required(redirect_field_name='/login/')
def addpost(request):
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            form = AddPost()
            return redirect('Post:index')

    else:
        form = AddPost()  
    context = {"form":form}
    return render(request,'post/addnew.html',context)

def detail(request,post_id):
    single_post = Post.objects.get(id=post_id)
    context = {"single_post" : single_post,}
    return render(request,'post/detail.html',context)
class searchresultsview(ListView):
    model = Post
    template_name = 'post/search_results.html'
    
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(text__icontains=query)
        )
        return object_list
