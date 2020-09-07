from django.urls import path, include
from django.shortcuts import render
from rest_framework import routers
from .views import MovieViewSet, RatingViewSet, UserViewSet

from . import views

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('movies', MovieViewSet)
router.register('ratings', RatingViewSet)

app_name = 'movies'

urlpatterns = [
    path('', include(router.urls)),
]
