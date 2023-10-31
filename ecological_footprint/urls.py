from django.urls import path
from . import views

urlpatterns = [
    path('', views.infosvehiculefoyer_view, name='home-page'),
]
