from django.urls import path, include
from rest_framework import routers
from .views import CategoriesViewSet, GenreViewSet


app_name = 'api'

v1_router = routers.DefaultRouter()
v1_router.register(r'categories', CategoriesViewSet, basename='categories')
v1_router.register(r'genres', GenreViewSet, basename='genres')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
