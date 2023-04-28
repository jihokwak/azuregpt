from django.contrib import admin
from django.urls import path, include
# Add these imports at the beginning of the file
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/chat/', include('chat.urls')),
]

# Add these lines at the end of the file, before urlpatterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)