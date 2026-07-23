from django.urls import path
from . import views

urlpatterns = [
    path('calcolatore/', views.calcolatore_view, name='calcolatore'),
    path('', views.index, name='index'),
]