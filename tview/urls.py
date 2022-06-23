from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'TView'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls', namespace='contact')),
    path('', include('pages.urls', namespace='pages')),
    path('__debug__/', include('debug_toolbar.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)