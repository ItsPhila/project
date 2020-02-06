from django.contrib import admin
from django.urls import path, include
from main.views import IndexView
import main.urls

urlpatterns = [
    path('', IndexView.as_view()),
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('signup/', include('users.urls')),
    path('', include('main.urls', namespace = 'main')),
    path('', include('django.contrib.auth.urls')),



]
