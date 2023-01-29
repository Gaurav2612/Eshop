from random import choices
from django.db import models
from datetime import datetime

class Maincategory(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Seller(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=20)
    addressline1 = models.CharField(max_length=100, default = None, blank=True, null=True)
    addressline2 = models.CharField(max_length=100, default = None, blank=True, null=True)
    addressline3 = models.CharField(max_length=100, default = None, blank=True, null=True)
    pin = models.CharField(max_length=100, default = None, blank=True, null=True)
    city = models.CharField(max_length=100, default = None, blank=True, null=True)
    state = models.CharField(max_length=100, default = None, blank=True, null=True)
    pic = models.ImageField(upload_to = "images/", default = None, blank=True, null=True)
    def __str__(self):
        return self.name

class Buyer(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=20)
    addressline1 = models.CharField(max_length=100, default = None, blank=True, null=True)
    addressline2 = models.CharField(max_length=100, default = None, blank=True, null=True)
    addressline3 = models.CharField(max_length=100, default = None, blank=True, null=True)
    pin = models.CharField(max_length=100, default = None, blank=True, null=True)
    city = models.CharField(max_length=100, default = None, blank=True, null=True)
    state = models.CharField(max_length=100, default = None, blank=True, null=True)
    pic = models.ImageField(upload_to = "media/images/", default = None, blank=True, null=True)
    def __str__(self):
        return self.username

class Product(models.Model):
    name = models.CharField(max_length=50)
    maincategory = models.ForeignKey(Maincategory,on_delete = models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete= models.CASCADE)
    basePrice = models.IntegerField()
    discount = models.IntegerField()
    finalPrice = models.IntegerField()
    color = models.CharField(max_length=20)
    size = models.CharField(max_length = 20)
    description = models.TextField()
    stock = models.CharField(max_length = 20)
    date = models.DateTimeField(auto_now=True)
    pic1 = models.ImageField(upload_to = "media/images/", default = None, blank=True, null=True)
    pic2 = models.ImageField(upload_to = "media/images/", default = None, blank=True, null=True)
    pic3 = models.ImageField(upload_to = "media/images/", default = None, blank=True, null=True)
    pic4 = models.ImageField(upload_to = "media/images/", default = None, blank=True, null=True)
    def __str__(self):
        return self.name


class Wishlist(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)+" "+self.user.name


""" class Newslatter(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length = 50)  
    def __str__(self):
        return str(self.id)+" "+str(self.email) """



choice = ((1,"Not Packed"),(2,"Packed"),(3,"Out for Delivery"),(4,"Delivered"))
paymentChoice = ((1,"Pending"),(2,"Done"))
class Checkout(models.Model):
    id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    total = models.IntegerField(default=0,null=True,blank=True)
    shipping = models.IntegerField(default = 0,null=True,blank=True)
    final = models.IntegerField(default=0,null=True,blank=True)
    mode = models.CharField(max_length = 20,default = "COD", null=True,blank=True)
    status = models.IntegerField(choices = choice,default=1)
    paymentStatus = models.IntegerField(choices=paymentChoice,default=1)
    active = models.BooleanField(default=True)
    #paymentmode = models.CharField(max_length = 20,default = "COD", null=True,blank=True)
    #paymentstatus = models.CharField(max_length=20,default="Pending",null=True,blank=True)
    #orderstatus = models.CharField(max_length = 20,default = "Not Packed", null=True,blank=True)
    date = models.DateTimeField(auto_now=True)
    rppid = models.CharField(max_length = 50,default = "", null=True,blank=True)
    rpoid = models.CharField(max_length = 50,default = "", null=True,blank=True)
    rpsid = models.CharField(max_length = 50,default = "", null=True,blank=True)
    

    def __str__(self):
        return str(self.id)+" "+self.buyer.username


class CheckoutProducts(models.Model):
    id = models.AutoField(primary_key=True)
    productid = models.IntegerField()
    q = models.IntegerField(default=1)
    total = models.IntegerField(default=0)
    checkout = models.ForeignKey(Checkout,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return "id = "+str(self.id)+"  "+"checkout_id = "+str(self.checkout.id)



class Newslatter(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length = 50,unique=True)

    def __str__(self):
        return self.email


contactStatusChoice = ((1,"Active"),(2,"Done"))
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length = 50)
    phone = models.CharField(max_length=15)
    subject = models.TextField()
    message = models.TextField()
    status = models.IntegerField(choices = contactStatusChoice, default=1)

    def __str__(self):
        return self.email