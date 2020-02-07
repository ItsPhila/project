from django.contrib import admin
from django.urls import path, include
from main.views import IndexView
from django.conf.urls import handler404, handler500
from django.conf import settings  
from django.conf.urls.static import static
import main.urls

urlpatterns = [
    path('', IndexView.as_view()),
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('places/', include('places.urls')),
    path('signup/', include('users.urls')),
    path('', include('main.urls', namespace = 'main')),
    path('', include('django.contrib.auth.urls')),


]

handler404 = 'main.views.page_not_found'
handler500 = 'main.views.server_error'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)