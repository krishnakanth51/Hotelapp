
from django.db import models

#Create your models here.
class  application(models.Model):
    Platinum=models.CharField(max_length=44)
    suit=models.CharField(max_length=52)
    gold=models.CharField(max_length=60)
    Ordinary=models.CharField(max_length=55)

class Signup (models.Model):
    TYPES=(
    (0,"premium"),
    (1,"nonpremium"),    
    )
    Customer_name=models.CharField(max_length=20)
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=22)

class login (models.Model):
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=22)


# Create your models here.

class signup(models.Model):
    TYPES = (
    (0,"premium"),
    (1,"nonpremium"),
	)
    customer_name = models.CharField(max_length =50)
    username = models.CharField(max_length =50)
    password = models.CharField(max_length =50)
    membershiptype = models.CharField(max_length=20, choices=TYPES)

class Rent(models.Model):
    customerid = models.AutoField(db_column='RentID', primary_key=True)  # Field name made lowercase.
    checkin = models.DateTimeField(db_column='From_Date', blank=True, null=True,verbose_name='Check-In Date')  # Field name made lowercase.
    checkout = models.DateTimeField(db_column='To_Date', blank=True, null=True, verbose_name='Check-Out Date')  # Field name made lowercase.
    isactive = models.NullBooleanField(db_column='ISactive')  # Field name made lowercase.
    roomtype = models.CharField(db_column='RoomType', max_length=20, blank=True, null=True,verbose_name='Type')

    def __str__(self):
        return self.account
    class Meta:
        managed = True
        db_table = 'Rent'


class Booking(models.Model):
    bookingid = models.AutoField(db_column='BookingID', primary_key=True)  # Field name made lowercase.
    
    class Meta:
        managed = True
        db_table = 'Booking'"""


# 1. Customer-id

# 2. Membership-type

# 3. Booking-id

# 4. ReservedRoom type















