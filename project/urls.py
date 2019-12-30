from django.contrib import admin
from django.urls import path, include
from main.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('signup/', include('users.urls')),
    path('', include('main.urls')),
    path('', include('django.contrib.auth.urls')),



]
