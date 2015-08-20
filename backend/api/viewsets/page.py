from ..serializers import PageListSerializer, PageDetailSerializer
from rest_framework.viewsets import ModelViewSet
from pages.models import Page
from .utils import MultiSerializerViewSet


class PageViewSet(MultiSerializerViewSet):
    model = Page
    queryset = Page.objects.filter(is_enabled=True)

    serializers = {
        'default': PageListSerializer,
        'retrieve': PageDetailSerializer,
    }

    lookup_field = 'slug'
    lookup_value_regex = '[0-9a-z_]+'
