from inspect import ArgSpec
from django.db import models
from django.utils.text import slugify
FIELD_CHOICE=(
    ("physical", "physical"),
    ("digital" ,"digital"),
    )
# Create your models here.
class Product(models.Model):
    FIELD_CHOICE=(
    ("physical", "physical"),
    ("digital" ,"digital"),
    )
    name=models.CharField( max_length=200)
    """
        127.0.0.1/8000/products/
        127.0.0.1:8000/product/1/ detail of product with id 1
    """
    slug = models.SlugField(unique=True, max_length=200, blank = True, null = True) 
    # auto generated
    # price = models.FloatField()
    # image = models.ImageField(upload_to="images") require pillow package
    price=models.DecimalField(max_digits=10, decimal_places=2)
    created_at=models.DateField(auto_now_add=True)
    modified_at=models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)
    product_type=models.CharField(max_length=15, choices=FIELD_CHOICE)
    category=models.ForeignKey('Category',on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.name
     
    def save(self, *args, **kwargs): 
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)




class Category(models.Model):
    name=models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add=True) # created date
    modified_at=models.DateField(auto_now=True) # updated data for each update

    def __str__(self):
        return self.name