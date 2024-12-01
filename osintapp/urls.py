from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_view, name='search'),  # Main search page
    path('bookmark/', views.bookmark_result, name='bookmark'),  # Bookmarking results
    path('bookmarks/', views.view_bookmarks, name='bookmarks'),  # View bookmarks
]
