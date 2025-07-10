from django.db import models

from django.core.validators import MinValueValidator
from decimal import Decimal

from core.models import BaseModel


class Category(BaseModel):
    """
    Category model
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return self.name


class Tag(BaseModel):
    """
    Tag model for product labeling
    """
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.name}"


class Product(BaseModel):
    """
    Product model.
    """
    
    # Basic product information
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    product_category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='products'
    )
    tags = models.ManyToManyField(
        Tag, 
        blank=True, 
        related_name='products'
    )

    def __str__(self):
        return f"{self.id} - {self.name}"
