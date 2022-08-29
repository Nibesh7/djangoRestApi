from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
    # or
# from .views import api_home



# app_name = 'api'

urlpatterns = [
    path('',views.api_home),
    path('auth/',obtain_auth_token)
]