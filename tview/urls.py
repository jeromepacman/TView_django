from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'TView'
admin.site.site_title = 'Admin'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sendmail/', include('sendmail.urls', namespace='sendmail')),
    path('', include('pages.urls', namespace='pages'))
]

