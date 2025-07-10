from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from .models import Product, Category, Tag
from .forms import ProductSearchForm


class ProductListView(ListView, FormMixin):
    """
    View for displaying products with search and filter functionality.
    """
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 12
    form_class = ProductSearchForm
    
    def get_queryset(self):
        """Get filtered and sorted queryset based on form data."""
        queryset = Product.objects.all().select_related('product_category').prefetch_related('tags')
        
        # Get form data
        form = self.get_form()
        if form.is_valid():
            search = form.cleaned_data.get('search')
            category = form.cleaned_data.get('product_category')
            tags = form.cleaned_data.get('tags')
            min_price = form.cleaned_data.get('min_price')
            max_price = form.cleaned_data.get('max_price')
            sort_by = form.cleaned_data.get('sort_by')
            
            # Apply filters
            if search:
                queryset = queryset.filter(
                    Q(name__icontains=search) |
                    Q(description__icontains=search)
                )
            
            if category:
                # Include products from subcategories
                categories = [category] + list(category.children.all())
                queryset = queryset.filter(product_category__in=categories)
            
            if tags:
                queryset = queryset.filter(tags__in=tags).distinct()
            
            if min_price:
                queryset = queryset.filter(price__gte=min_price)
            
            if max_price:
                queryset = queryset.filter(price__lte=max_price)
            
            # Apply sorting
            if sort_by:
                queryset = queryset.order_by(sort_by)
        
        return queryset
    
    def get_form_kwargs(self):
        """Pass GET parameters to form."""
        kwargs = super().get_form_kwargs()
        kwargs['data'] = self.request.GET or None
        return kwargs
    
    def get_context_data(self, **kwargs):
        """Add additional context data."""
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['total_products'] = self.get_queryset().count()
        
        # Add filter counts for sidebar
        context['categories'] = Category.objects.all()
        
        context['tags'] = Tag.objects.all()
        
        return context
