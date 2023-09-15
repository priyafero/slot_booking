from rest_framework import routers
from django.urls import path, include
from . import views

slot_booking_router = routers.DefaultRouter()
slot_booking_router.register(r'customers', views.CustomerViewSet)
# Add similar lines for other models

urlpatterns = [
    path('', include(slot_booking_router.urls)),
]
