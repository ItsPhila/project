
from .views import index, detail, addpost
from django.urls import path
app_name = 'Post'
urlpatterns = [
    path('', index, name ='index'),
    path('addnew', addpost, name ='addnew'),
    path('<int:post_id>', detail, name ="detail"),
]
