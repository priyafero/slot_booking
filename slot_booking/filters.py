from django_filters import rest_framework as filters

from slot_booking.models import Trip, Customer, Warehouse, Driver, Vehicle, Timeslot, Order


class TripFilter(filters.FilterSet):
    class Meta:
        model = Trip
        fields = ("status", "driver")


class CustomerFilter(filters.FilterSet):
    class Meta:
        model = Customer
        fields = ("name",)


class WarehouseFilter(filters.FilterSet):
    class Meta:
        model = Warehouse
        fields = ("name",)


class DriverFilter(filters.FilterSet):
    class Meta:
        model = Driver
        fields = ("name", 'vehicles')


class VehicleFilter(filters.FilterSet):
    class Meta:
        model = Vehicle
        fields = ("vehicle_number",)


class TimeslotFilter(filters.FilterSet):
    class Meta:
        model = Timeslot
        fields = ("driver", 'warehouse', 'trip', 'status')


class OrderFilter(filters.FilterSet):
    class Meta:
        model = Order
        fields = ("customer", 'warehouse', 'trip', 'status')
