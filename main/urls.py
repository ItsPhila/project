from .views import home
from django.urls import path


app_name = 'Main'
urlpatterns = [
    path('',home, name ='index'),
]

