from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('threatintel.urls')),  # Include your app URLs
    path('accounts/', include('allauth.urls')),  # Allauth URLs
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout URL
]