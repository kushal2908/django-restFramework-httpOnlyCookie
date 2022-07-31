from django.urls import include
from django.contrib import admin
from django.urls import path
from cookieapp.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cookieapp.urls')),  # new
]
