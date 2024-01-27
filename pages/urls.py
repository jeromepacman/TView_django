from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('prod/', views.ProdView.as_view(), name="prod"),
    path('infos/', views.InfosView.as_view(), name="infos"),
    path('', views.HomeView.as_view(), name="home")

]
