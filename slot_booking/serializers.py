from . import models

from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Customer
        fields = (
            "id",
            "name",
            "address",
            "contact",
            "from_time",
            "to_time"
        )


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Vehicle
        fields = (
            "id",
            "vehicle_number",
        )


class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Driver
        fields = (
            "id",
            "name",
            "shift_start",
            "shift_end",
            "contact"
        )


class WareHouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Warehouse
        fields = (
            "id",
            "address",
            "to_time",
            "from_time",
        )


class TimeSlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Timeslot
        fields = (
            "id",
            "starttime",
            "endtime",
            "driver",
            "warehouse",
            "trip",
            "status"
        )