from django.db import models 
from django.contrib.auth.models import User

# Create your models here.
class CustomManager(models.Manager):
    def mobile_list(self):
        return self.filter(category__exact="Mobile")
    
    def electronics_list(self):
        return self.filter(category__exact="Electronics")
    
    def pricerange(self, r1, r2):
        return self.filter(price__range=(r1, r2))

class Product(models.Model):
    userid=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    productid=models.IntegerField(primary_key=True)
    productname=models.CharField(max_length=60)
    type=(
        ('Mobile','Mobile'),('cloths','cloths'),('shoes','shoes'),('Electronic','Electronic'),
    )
    category = models.CharField(max_length=50, choices=type)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="photos")
    objects = models.Manager()
    productmanager = CustomManager()

class cart(models.Model):
    userid=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    productid=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=0)

class Order(models.Model):
    orderid = models.IntegerField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    qty = models.PositiveIntegerField(default=0)    



