from ..serializers import CategoryListSerializer, CategoryDetailSerializer
from rest_framework.viewsets import ModelViewSet
from photos.models import Category
from django.db.models import Count
from .utils import MultiSerializerViewSet


class CategoryViewSet(MultiSerializerViewSet):
    model = Category
    queryset = Category.objects.annotate(photos_count=Count('photo'))\
        .filter(photos_count__gte=1, is_enabled=True, )

    serializers = {
        'default': CategoryListSerializer,
        'retrieve': CategoryDetailSerializer,
    }

    lookup_field = 'slug'
    lookup_value_regex = '[0-9a-z\-_]+'
