from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
      url('admin/', admin.site.urls),
      url(r'^', include('rem.urls', namespace='rem')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
