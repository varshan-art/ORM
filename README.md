# Ex01 Django ORM Web Application
## Date: 31-01-2026

## AIM
To develop a Django Application to store and retrieve data from an Online Food Delivery Database platform like Zomato or Swiggy using Object Relational Mapping(ORM).
## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
models.py
from django.db import models
from django.contrib import admin
class zomatoDB(models.Model):
    Name=models.CharField(max_length=25);
    Address=models.CharField(max_length=100);
    Email=models.EmailField();
    Mobile_no=models.IntegerField();
    OTP=models.IntegerField(primary_key=True);
    Time=models.TimeField();
    Ratings=models.FloatField();
    Amount=models.FloatField();
class DeliveryDBAdmin(admin.ModelAdmin):
	list_display=['Name','Address','Email','Mobile_no','OTP','Time','Ratings','Amount'];

admin.py
from django.contrib import admin
from .models import zomatoDB,DeliveryDBAdmin
admin.site.register(zomatoDB,DeliveryDBAdmin)
```





## OUTPUT

![alt text](<Screenshot 2026-01-31 113703.png>)



## RESULT
Thus the program for creating retrieve data from an Online Food Delivery Database platform like Zomato or Swiggy database using ORM hass been executed successfully
