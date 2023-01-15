from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=100, unique=True)
    slug=models.SlugField(max_length=100, unique=True) 
    description=models.TextField(blank=True, max_length=255)
    cat_img = models.ImageField(blank=True, upload_to='photos/category')

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=256,unique=True)
    slug = models.SlugField(max_length=256,unique=True)
    description = models.TextField()
    price= models.IntegerField(null=True, blank=True)
    images = models.ImageField(upload_to='photos/products',blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    model_no = models.CharField(max_length=255, blank=True, null=True)
    stock = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.FileField(upload_to="products")