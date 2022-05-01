from django.db import models

class Driver(models.Model):
    firstName = models.CharField(max_length=50, blank=False, default=0)
    lastName = models.CharField(max_length=50, blank=False, default=0)
    # birtdate
    phone = models.CharField(max_length=20, blank=False, default=0)
    telegram = models.CharField(max_length=20, blank=False, default=0)
    mc = models.CharField(max_length=10, blank=True) # MC number
    usdot = models.CharField(max_length=10, blank=True) # DOT number
    cdl = models.CharField(max_length=10, blank=True) # CDL number
    vin = models.CharField(max_length=10, blank=True) # VIN number
    trailer = models.CharField(max_length=10, blank=True) # Trailer number
    address = models.TextField(max_length=500, blank=True)
    state = models.CharField(max_length=2, blank=False, default=0)
    gRate = models.FloatField(blank=False, default=0) # my percentage from gross


class Customer(models.Model):
    firstName = models.CharField(max_length=50, blank=False, default=0)
    lastName = models.CharField(max_length=50, blank=False, default=0)
    phone = models.CharField(max_length=20, blank=False, default=0)
    telegram = models.CharField(max_length=20, blank=False, default=0)
    mc = models.CharField(max_length=10, blank=True)
    usdot = models.CharField(max_length=10, blank=True)
    companyName = models.CharField(max_length=50, blank=True)
    entity = models.CharField(max_length=20, blank=True) # broker or shipper or else?
    address = models.TextField(max_length=500, blank=True)
    state = models.CharField(max_length=2, blank=False, default=0)

class Order(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.RESTRICT, related_name='orders', null=False)
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, related_name='orders', null=False)
    originState = models.CharField(max_length=2, blank=False, default=0)
    originAddress = models.TextField(max_length=500, blank=False, default=0)
    originMarket = models.CharField(max_length=50, blank=False, default=0)
    destinationState = models.CharField(max_length=2, blank=False, default=0)
    destinationAddress = models.TextField(max_length=500, blank=False, default=0)
    destinationMarket = models.CharField(max_length=50, blank=False, default=0)
    pickupDate = models.DateTimeField(blank=False)
    deliveryDate = models.DateTimeField(blank=False)
    #dropoffdate or dropdate
    mileage = models.SmallIntegerField(blank=False, default=0)
    deadhead = models.SmallIntegerField(blank=False, default=0)
    gross = models.FloatField(blank=False, default=0)
    #gRate = driver.gRate
    fuelBurnt = models.FloatField(blank=False, default=0) # gallons
    fuelPrice = models.FloatField(blank=False, default=0) # USD per gallon
    toll = models.FloatField(blank=False, default=0)

class Document(models.Model):
    issueDate = models.DateTimeField()
    expiryDate = models.DateTimeField()
    entity = models.CharField(max_length=50, blank=False, default=0)
    result = models.CharField(max_length=50, blank=False, default=0)


#class Truck:
#    pass
# one-to-one relation with Driver
# color, year, make, model etc;
