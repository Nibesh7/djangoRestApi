from django.urls import path

from . import views
    # or
# from .views import api_home



# app_name = 'api'

urlpatterns = [
    path('',views.api_home)
]