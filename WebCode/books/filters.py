
import django_filters
from django_filters import CharFilter
from .models import Book

class SetOfFilters(django_filters.FilterSet):
    name = CharFilter(field_name = 'name', lookup_expr = 'icontains')
    
    class Meta:
        model = Book
        fields = ['category','price', 'ISBN', 'publication_year']