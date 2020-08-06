import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

# class avec les champs personnalisés pour le filtre
class ArticleFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="created", lookup_expr='gte')
	title = CharFilter(field_name='title', lookup_expr='icontains')
    
