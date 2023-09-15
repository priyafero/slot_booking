from rest_framework import routers
from django.urls import path, include
from . import views

slot_booking_router = routers.DefaultRouter()
slot_booking_router.register(r'customers', views.CustomerViewSet)
slot_booking_router.register(r'driver', views.DriverViewSet)
slot_booking_router.register(r'vehicle', views.VehicleViewSet)
slot_booking_router.register(r'warehouse', views.WarehouseViewSet)
slot_booking_router.register(r'time_slot', views.TimeslotViewSet)
slot_booking_router.register(r'driver_time_slot', views.DriverTimeslotAssignmentViewSet)
slot_booking_router.register(r'order', views.OrderViewSet)
slot_booking_router.register(r'trip', views.TripViewSet)
# Add similar lines for other models

urlpatterns = [
    path('', include(slot_booking_router.urls)),
]
