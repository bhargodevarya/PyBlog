from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import generics
# Create your views here.


def health_check(request):
    return HttpResponse('Healthy')

#TODO, implemet this
class BlogView(generics.ListAPIView):
    pass