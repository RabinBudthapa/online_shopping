from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)
    logo=models.CharField(max_length=200,blank=True)
    slug=models.CharField(max_length=500,unique=True)
    def __str__(self):
        return self.name

class Slider(models.Model):
    name=models.CharField(max_length=500)
    image=models.ImageField(upload_to='media')
    description=models.TextField(blank=True)
    rank=models.IntegerField()
    url=models.URLField(blank=True,max_length=500)
    def __str__(self):
       return self.name

class Ad(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')
    description=models.TextField()
    rank=models.IntegerField()
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')
    rank=models.IntegerField()
    slug = models.CharField(max_length=500,default="")
    def __str__(self):
        return self.name
STOCK=(('in_stock','In_Stock'),('out of stock','Out of Stock'))
LABELS=(('','default'),('new','new'),('sale','sale'),('hot','hot'))
class Product(models.Model):
    name = models.CharField(max_length=500)
    price=models.IntegerField()
    discounted_price=models.IntegerField(default=0)
    image=models.ImageField(upload_to='media')
    description=models.TextField(blank=True)
    specification=models.TextField(blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    stock = models.CharField(choices=STOCK,max_length=50)
    labels=models.CharField(choices=LABELS,max_length=50)
    slug = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name
class CustomerReview(models.Model):
    name=models.TextField(max_length=500)
    post=models.TextField(max_length=500)
    image=models.ImageField(upload_to='media')
    comment=models.TextField(max_length=500,blank=True)
    def __str__(self):
        return self.name
