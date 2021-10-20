from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic import TemplateView
from blog.views import health_check

urlpatterns = [
    path('health/', health_check),
    path('home/', TemplateView.as_view(template_name='blog/index.html'))
]