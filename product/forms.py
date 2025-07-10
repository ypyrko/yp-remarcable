from django import forms
from .models import Category, Tag


class ProductSearchForm(forms.Form):
    """
    Form for searching and filtering products.
    Supports text search, category filtering, tag filtering, and price range.
    """
    search = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search products...',
            'class': 'form-control',
            'id': 'search-input'
        })
    )
    
    product_category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label="All Categories",
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'category-select'
        })
    )
    
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'tag-checkbox'
        })
    )
    
    min_price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Min Price',
            'class': 'form-control',
            'step': '0.01'
        })
    )
    
    max_price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Max Price',
            'class': 'form-control',
            'step': '0.01'
        })
    )
    
    SORT_CHOICES = [
        ('name', 'Name (A-Z)'),
        ('-name', 'Name (Z-A)'),
        ('price', 'Price (Low to High)'),
        ('-price', 'Price (High to Low)'),
        ('-created_at', 'Newest First'),
        ('created_at', 'Oldest First'),
    ]
    
    sort_by = forms.ChoiceField(
        choices=SORT_CHOICES,
        required=False,
        initial='-created_at',
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )