from django.urls import path

from . import views

urlpatterns = [
    path('', views.webhooks_endpoint),
    path('payload', views.payload_endpoint)
]
