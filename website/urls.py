from django.urls import path
from . import views

urlpatterns = [
    path('website/', views.Home, name='website'),
]