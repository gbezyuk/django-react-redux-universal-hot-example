from ..serializers import PhotoSerializer
from rest_framework.viewsets import ModelViewSet
from photos.models import Photo


class PhotoViewSet(ModelViewSet):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.filter(is_enabled=True)
    lookup_field = 'slug'
    lookup_value_regex = '[0-9a-z_]+'
