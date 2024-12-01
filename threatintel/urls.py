from django.urls import path
from . import views

urlpatterns = [
    path('', views.fetch_threats, name='fetch_threats'),
    path('save/<str:threat_id>/', views.save_threat, name='save_threat'),
]
