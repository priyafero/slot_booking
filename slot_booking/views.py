from rest_framework import viewsets

from .filters import TripFilter, CustomerFilter, WarehouseFilter, DriverFilter, VehicleFilter, TimeslotFilter, \
    OrderFilter
from .models import Customer, Vehicle, Driver, Warehouse, Timeslot, Trip, Order, DriverVehicleAssignment, \
    DriverTimeslotAssignment
from .serializers import CustomerSerializer, VehicleSerializer, DriverSerializer, WareHouseSerializer, \
    TimeSlotSerializer, TripSerializer, OrderSerializer, DriverVehicleAssignmentSerializer, \
    DriverTimeslotAssignmentSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_class = CustomerFilter


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WareHouseSerializer
    filterset_class = WarehouseFilter


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filterset_class = DriverFilter


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filterset_class = VehicleFilter


class TimeslotViewSet(viewsets.ModelViewSet):
    queryset = Timeslot.objects.all()
    serializer_class = TimeSlotSerializer
    filterset_class = TimeslotFilter


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_class = OrderFilter


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    filterset_class = TripFilter


class DriverVehicleAssignmentViewSet(viewsets.ModelViewSet):
    queryset = DriverVehicleAssignment.objects.all()
    serializer_class = DriverVehicleAssignmentSerializer


class DriverTimeslotAssignmentViewSet(viewsets.ModelViewSet):
    queryset = DriverTimeslotAssignment.objects.all()
    serializer_class = DriverTimeslotAssignmentSerializer
