from django.core.management.base import BaseCommand
from product.models import Category, Tag, Product
import random


class Command(BaseCommand):
    help = 'Populate sample data: categories, tags, and products.'

    def handle(self, *args, **options):
        # Create categories
        category_names = ['Electronics', 'Books', 'Clothing', 'Home', 'Sports']
        categories = []
        for name in category_names:
            category, _ = Category.objects.get_or_create(name=name)
            categories.append(category)
        self.stdout.write(self.style.SUCCESS('Created categories.'))

        # Create tags
        tag_names = [
            'New', 'Sale', 'Popular', 'Limited', 'Eco', 'Premium', 'Budget',
            'Trending', 'Classic', 'Gift'
        ]
        tags = []
        for name in tag_names:
            tag, _ = Tag.objects.get_or_create(name=name)
            tags.append(tag)
        self.stdout.write(self.style.SUCCESS('Created tags.'))

        # Create products
        product_data = [
            {"name": "Wireless Headphones", "description": "Noise-cancelling over-ear headphones.", "price": 89.99, "category": categories[0]},
            {"name": "Smartphone", "description": "Latest model with advanced features.", "price": 699.99, "category": categories[0]},
            {"name": "E-Book Reader", "description": "Lightweight e-reader with high-resolution display.", "price": 129.99, "category": categories[1]},
            {"name": "Classic Novel", "description": "A timeless literary masterpiece.", "price": 14.99, "category": categories[1]},
            {"name": "Men's T-Shirt", "description": "100% cotton, available in various colors.", "price": 19.99, "category": categories[2]},
            {"name": "Women's Jeans", "description": "Slim fit, stretch denim.", "price": 49.99, "category": categories[2]},
            {"name": "Coffee Maker", "description": "Programmable drip coffee machine.", "price": 59.99, "category": categories[3]},
            {"name": "Blender", "description": "High-power blender for smoothies.", "price": 39.99, "category": categories[3]},
            {"name": "Yoga Mat", "description": "Non-slip, eco-friendly material.", "price": 24.99, "category": categories[4]},
            {"name": "Football", "description": "Official size and weight.", "price": 29.99, "category": categories[4]},
            {"name": "Bluetooth Speaker", "description": "Portable speaker with deep bass.", "price": 34.99, "category": categories[0]},
            {"name": "Cookbook", "description": "Over 100 delicious recipes.", "price": 22.99, "category": categories[1]},
            {"name": "Dress", "description": "Elegant evening dress.", "price": 79.99, "category": categories[2]},
            {"name": "Table Lamp", "description": "Modern design with LED bulb.", "price": 27.99, "category": categories[3]},
            {"name": "Running Shoes", "description": "Lightweight and comfortable.", "price": 59.99, "category": categories[4]},
            {"name": "Laptop", "description": "High-performance laptop for work and play.", "price": 999.99, "category": categories[0]},
            {"name": "Children's Book", "description": "Illustrated story for kids.", "price": 12.99, "category": categories[1]},
            {"name": "Jacket", "description": "Water-resistant outdoor jacket.", "price": 89.99, "category": categories[2]},
            {"name": "Vacuum Cleaner", "description": "Bagless vacuum with HEPA filter.", "price": 119.99, "category": categories[3]},
            {"name": "Tennis Racket", "description": "Lightweight graphite frame.", "price": 79.99, "category": categories[4]},
        ]
        for data in product_data:
            # possible to improve with bulk_create
            product = Product.objects.create(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            product_category=data["category"]
            )
            # Assign random tags to product
            product.tags.set(random.sample(tags, k=random.randint(1, 3)))
            
        self.stdout.write(self.style.SUCCESS('Created products.'))