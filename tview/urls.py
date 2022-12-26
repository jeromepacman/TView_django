from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'TView'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sendmail/', include('sendmail.urls', namespace='sendmail')),
    path('', include('pages.urls', namespace='pages')),
]