from photos.models import Category
from rest_framework.serializers import HyperlinkedModelSerializer
from .photo import PhotoSerializer;


class CategoryListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class CategoryDetailSerializer(CategoryListSerializer):
    photos = PhotoSerializer(many=True)
    class Meta(CategoryListSerializer.Meta):
        fields = ('name', 'slug', 'photos')
        depth = 1
