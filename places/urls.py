from .views import addplace, index, detail
from django.urls import path
app_name = 'Place'
urlpatterns = [
    path('', index, name ='index'),
    path('addplace', addplace, name ='addplace'),
    path('<int:place_id>', detail, name ="detail"),
    
]
