from django_filters import rest_framework as filters
from .models import Brend


class BrendFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Brend
        fields = ['name', 'id']
