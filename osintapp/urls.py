from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_redirect, name='home'),
    path('search/', views.search_view, name='search'),
    path('bookmark/', views.bookmark_result, name='bookmark'),
    path('bookmarks/', views.view_bookmarks, name='bookmarks'),
    path('register/', views.register, name='register'),
]
