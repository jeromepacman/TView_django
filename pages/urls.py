from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('you/', views.PersoView.as_view(), name="perso"),
    path('shop/', views.ShopView.as_view(), name="boutique"),
    path('applications/', views.ProView.as_view(), name="pro"),
    path('infos/', views.InfosView.as_view(), name="infos"),
]