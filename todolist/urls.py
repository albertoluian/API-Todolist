from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('task.urls')),
]
