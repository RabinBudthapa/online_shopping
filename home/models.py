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

class Cart(models.Model):
    username = models.CharField(max_length=300)
    slug = models.CharField(max_length=500)
    quantity = models.FloatField()
    total = models.FloatField()
    items = models.ForeignKey(Product,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    checkout = models.BooleanField(default=False)
    def __str__(self):
        return self.username

class Wishlist(models.Model):
    username = models.CharField(max_length=300)
    slug = models.CharField(max_length=500)
    items = models.ForeignKey(Product,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    checkout = models.BooleanField(default=False)
    def __str__(self):
        return self.username

class ProductReview(models.Model):
    username = models.CharField(max_length=300)
    slug = models.CharField(max_length=500)
    star = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class CustomerAddress(models.Model):
    firstname = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    phonenumber = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    def __str__(self):
        return self.firstname


