
from .views import index, detail, addpost, searchresultsview
from django.urls import path
app_name = 'Post'
urlpatterns = [
    path('', index, name ='index'),
    path('addnew', addpost, name ='addnew'),
    path('<int:post_id>', detail, name ="detail"),
    path('search', searchresultsview.as_view(), name ='search_results'),
]
