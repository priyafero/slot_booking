# Register your models here.
from django.contrib import admin

from .models import Customer, Warehouse, Driver, Vehicle, Timeslot, Trip, Order, DriverVehicleAssignment, \
    DriverTimeslotAssignment


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'from_time', 'to_time', 'contact')


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'from_time', 'to_time')


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'shift_start', 'shift_end')


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_number',)


@admin.register(Timeslot)
class TimeslotAdmin(admin.ModelAdmin):
    list_display = ('starttime', 'endtime', 'driver', 'warehouse', 'trip', 'status')


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'status', 'driver')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_no', 'packages', 'weight', 'customer', 'warehouse', 'trip', 'status')


@admin.register(DriverVehicleAssignment)
class DriverVehicleAssignmentAdmin(admin.ModelAdmin):
    list_display = ('driver', 'vehicle',)


@admin.register(DriverTimeslotAssignment)
class DriverTimeslotAssignmentAdmin(admin.ModelAdmin):
    list_display = ('driver', 'timeslot',)
