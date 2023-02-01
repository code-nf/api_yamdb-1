from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import UsersViewSet, APIGetToken, APISignup

v1_router = DefaultRouter()
v1_router.register(r'users', UsersViewSet, basename='users')

urlpatterns = [
    path('v1/auth/token/', APIGetToken.as_view(), name='get_token'),
    path('v1/', include(v1_router.urls)),
    path('v1/auth/signup/', APISignup.as_view(), name='signup'),
]
