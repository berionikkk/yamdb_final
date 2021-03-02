from django_filters.rest_framework import filterset, filters
from .models import Title


class TitleFilter(filterset.FilterSet):
    genre = filters.CharFilter(field_name="genre__slug")
    category = filters.CharFilter(field_name="category__slug")
    year = filters.CharFilter(field_name="year")
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Title
        fields = ["genre", "category", "year", "name"]
