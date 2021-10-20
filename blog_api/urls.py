from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from blog_api.views import BlogView, health_check

urlpatterns = [
    path('health', health_check),
    path('list', BlogView.as_view(), name="list blog")
]