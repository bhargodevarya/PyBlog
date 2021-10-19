from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from blog.views import health_check

urlpatterns = [
    path('health/', health_check),
]