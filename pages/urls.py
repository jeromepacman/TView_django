from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('you/', views.YouView.as_view(), name="you"),
    path('shop/', views.ShopView.as_view(), name="shop"),
    path('applications/', views.AppsView.as_view(), name="apps"),
    path('infos/', views.InfosView.as_view(), name="infos"),
    path('contact/', views.ContactView.as_view(), name="contact"),
]