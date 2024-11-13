from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todoapps.urls')),  # Include URLs from the todoapps app
]
