from django.urls import path
from rest_framework import routers
from .viewsets import CustomUserViewsets,RegisterViewSet,LoginViewSet,RefreshViewset
# from .views import (sign_in,sign_out,sign_up)

# urlpatterns = [
#     path('login/', sign_in, name='login'),
#     path('logout/', sign_out, name='logout'),
#     path('signup/', sign_up, name='signup'),
# ]

router=routers.SimpleRouter()

router.register(r'user', CustomUserViewsets, basename='user')
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'refresh', RefreshViewset, basename='auth-refresh')

urlpatterns=[
    *router.urls
]