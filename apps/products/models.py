from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from apps.users.models import User

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    categories = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.PositiveIntegerField(validators=[
            MinValueValidator(1, message="El precio debe ser al menos $1."),
            MaxValueValidator(1000000, message="El precio no puede exceder $1.000.000."),
        ])
    description = models.TextField()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name


class ShoppingCart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='shopping_cart')
