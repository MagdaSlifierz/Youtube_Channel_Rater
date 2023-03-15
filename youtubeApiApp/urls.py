from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import YoutubeChannelViewSet, RatingsViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('youtubeChannel', YoutubeChannelViewSet)
router.register('ratings', RatingsViewSet)
router.register('user', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
