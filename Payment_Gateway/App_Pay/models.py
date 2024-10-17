from django.db import models

# Create your models here.



class ColdCoffee(models.Model):
    name = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    order_id = models.CharField(max_length=100, blank=True)
    rezorpay_payment_id = models.CharField(max_length=100, blank= True)
    paid = models.BooleanField(default=False)
    
    
    
    
    
    