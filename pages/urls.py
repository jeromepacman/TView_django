from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('perso/', views.PersoView.as_view(), name="perso"),
    path('boutique/', views.ShopView.as_view(), name="boutique"),
    path('pro/', views.ProView.as_view(), name="pro"),
    path('infos/', views.InfosView.as_view(), name="infos"),
    path('', views.HomeView.as_view(), name="home"),
]