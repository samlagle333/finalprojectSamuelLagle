from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Show the custom homepage
    path('register/', views.register, name='register'),
    path('search/', views.search_view, name='search'),
    path('bookmark/', views.bookmark_result, name='bookmark'),
    path('bookmarks/', views.view_bookmarks, name='bookmarks'),
    path('logout/', views.custom_logout, name='logout'),
    path('check_dck/', views.check_dck, name='check_dck'),
    path('check_about/', views.check_about, name='check_about'),
]
