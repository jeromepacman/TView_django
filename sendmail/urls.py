from django.urls import path

from .views import sendmail_view

app_name = 'sendmail'
urlpatterns = [
    path('', sendmail_view, name='sendmail'),
]