from django.urls import path

from .views import sendmailView

app_name = 'sendmail'
urlpatterns = [
    path('', sendmailView, name='sendmail'),
]