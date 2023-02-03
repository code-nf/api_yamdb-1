from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from rest_framework import routers
from .views import CategoriesViewSet, GenreViewSet, TitlesViewSet
from api.views import UsersViewSet, APIGetToken, APISignup


app_name = 'api'

v1_router = DefaultRouter()
v1_router.register(r'users', UsersViewSet, basename='users')
v1_router.register(r'categories', CategoriesViewSet, basename='categories')
v1_router.register(r'genres', GenreViewSet, basename='genres')
v1_router.register(r'titles', TitlesViewSet, basename='titles')

urlpatterns = [
    path('v1/auth/token/', APIGetToken.as_view(), name='get_token'),
    path('v1/', include(v1_router.urls)),
    path('v1/auth/signup/', APISignup.as_view(), name='signup'),
]
