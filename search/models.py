from django.db import models

# Create your models here.
class Listing(models.Model):
    bidCount = models.FloatField(blank=True,null=True)
    buyItNowPrice = models.FloatField(blank=True,null=True)
    currentPrice = models.FloatField(blank=True,null=True)
    imageURL = models.URLField(blank=True,null=True)
    itemId = models.CharField(max_length=220, blank=True,null=True)
    primaryCategoryName = models.CharField(max_length=220, blank=True,null=True)
    primaryCategoryId = models.CharField(max_length=220, blank=True,null=True)
    shippingCost = models.FloatField(blank=True,null=True)
    endTime = models.CharField(max_length=220, blank=True,null=True)
    title = models.CharField(max_length=220, blank=True,null=True)
    viewItemURL = models.URLField(blank=True,null=True)
    watchCount = models.FloatField(blank=True,null=True)