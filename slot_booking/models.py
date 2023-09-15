from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=100)
    from_time = models.TimeField(max_length=100)
    to_time = models.TimeField(max_length=100)

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    from_time = models.TimeField(max_length=100)
    to_time = models.TimeField(max_length=100)

    def __str__(self):
        return self.name


class Driver(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=100)
    vehicles = models.ManyToManyField('Vehicle', through='DriverVehicleAssignment')
    shift_start = models.TimeField(max_length=100)
    shift_end = models.TimeField(max_length=100)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=255)

    def __str__(self):
        return self.vehicle_number


class DriverVehicleAssignment(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.driver.name} - {self.vehicle.name}"


class DriverTimeslotAssignment(models.Model):
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    timeslot = models.ForeignKey('Timeslot', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.driver.name} - {self.timeslot.starttime} to {self.timeslot.endtime}"


class Timeslot(models.Model):
    STATUS_CHOICES = [
        ('booked', 'Booked'),
        ('available', 'Available'),
    ]

    starttime = models.TimeField(max_length=100)
    endtime = models.TimeField(max_length=100)
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE)
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.starttime} - {self.endtime} ({self.status})"


class Trip(models.Model):
    STATUS_CHOICES = [
        ('schedule', 'Scheduled'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('pause', 'Paused'),
    ]

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.start_time} - {self.end_time} ({self.status})"


class Order(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('unassigned', 'Unassigned'),
        ('assigned', 'Assigned'),
        ('enroute', 'Enroute'),
        ('delivered', 'Delivered'),
        ('not_delivered', 'Not Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    order_no = models.CharField(max_length=20, unique=True)
    packages = models.PositiveIntegerField(default=1)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE)
    trip = models.ForeignKey('Trip', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return f"Order No: {self.order_no} ({self.status})"
