from .views import getuuids
from django.urls import path

urlpatterns = [
    path('', getuuids),
]
