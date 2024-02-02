from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _

admin.site.site_header = 'TView'
admin.site.site_title = 'Admin'


urlpatterns = i18n_patterns(
path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('sendmail/', include('sendmail.urls', namespace='sendmail')),
    path('', include('pages.urls', namespace='pages'))
)

