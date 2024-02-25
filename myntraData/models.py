from django.db import models
from myntraData.choices import *

class Carousel(models.Model):
    img = models.URLField(max_length=200)
    
class Product(models.Model):
    brandName = models.CharField(max_length=100)
    catName = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100)
    clothingType = models.CharField(choices=clothing_category, max_length=20)
    ProductTo = models.CharField(choices=product_to_choices, max_length=10)
    name = models.CharField(max_length=100)
    offerPrice = models.DecimalField(max_digits=10, decimal_places=2)
    oldPrice = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=100)
    thumbImg = models.URLField(max_length=500)
    description = models.TextField()

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', default="")
    image = models.URLField(max_length=200)
    alt = models.CharField(max_length=100)

class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='size', default="")
    size = models.CharField(max_length=10)

class ProductDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='productDetails', default="")
    product_material_detail = models.TextField()

class SizeFit(models.Model):
    product_detail = models.ForeignKey(ProductDetail, on_delete=models.CASCADE, related_name='sizefit', default="")
    title = models.CharField(max_length=100)

class MaterialCare(models.Model):
    product_detail = models.ForeignKey(ProductDetail, on_delete=models.CASCADE, related_name='materialcare', default="")
    title = models.CharField(max_length=100)
    
class User(models.Model):
    user_email = models.EmailField(unique=True,null=True, blank=True)
    password = models.CharField(max_length=12,null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    pin_code = models.IntegerField(null=True, blank=True)
   
class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, default="") 
    name = models.CharField(max_length=20)
    pincode = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    town = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    addressType = models.CharField(max_length=20)
    isDefault = models.BooleanField() 
    
class WishLists(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, default="") 
    product_id = models.IntegerField()
    
class CartItems(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, default="") 
    product_id = models.IntegerField()
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=1)
    
class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE,related_name="comments", default="")
    user = models.ForeignKey(User, on_delete = models.CASCADE, default="")
    img = models.URLField(max_length=200, null=True)
    message = models.TextField(null=False)
    date = models.DateField(auto_now=True) 
    
class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE,related_name="ratings", default="")
    rating = models.IntegerField()
    
class BoughtProduct(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, default="")
  
class ProductId(models.Model):
    bought_product = models.ForeignKey(BoughtProduct, on_delete=models.CASCADE, default ="", related_name="productIds")
    productId = models.IntegerField()
class Category(models.Model):
    categoryName = models.CharField(max_length=30, null=True)
    category = models.CharField(max_length=30, null=True)
    offer = models.CharField(max_length=20)
    brand = models.CharField(max_length=20, null=True)
    img = models.URLField(max_length=200, null=True)
    
class Search(models.Model):
    name = models.CharField(max_length=30, null=True)
    
class Question(models.Model):
    text = models.CharField(max_length=30, null=True)
    
class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE, default="")
    choice_text = models.CharField(max_length=200, default="")
     
class BrandCategory(models.Model):
    img = models.URLField(max_length=200)
    brandNameImg = models.URLField(max_length=200, default="")
    brandName = models.CharField(max_length=50)
    offer = models.CharField(max_length=20)
    
class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_info")
    full_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    birthday = models.CharField(max_length=10)
    alternate_mobile_number = models.IntegerField()
    hint = models.CharField(max_length=20)
    
    
    
