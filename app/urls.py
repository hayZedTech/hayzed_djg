from django.urls import path,include
from .views import PostViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView


router = DefaultRouter()
router.register("post", PostViewSet)

urlpatterns=[
    path("", include(router.urls)),
    path("auth-token/", obtain_auth_token),
    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path("api/logout/", TokenBlacklistView.as_view()),
]