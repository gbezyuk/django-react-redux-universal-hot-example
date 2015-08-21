from photos.models import Photo
from rest_framework.serializers import HyperlinkedModelSerializer
from .utils import MyImageField


class PhotoSerializer(HyperlinkedModelSerializer):
    image = MyImageField()

    class Meta:
        model = Photo
        fields = ('name', 'slug', 'image')
