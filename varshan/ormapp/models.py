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