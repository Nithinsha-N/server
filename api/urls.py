from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .viewset import *
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'ticket', TicketViewSet, basename='ticket')
app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
]
urlpatterns += [path('token/', obtain_auth_token, name="login")]
