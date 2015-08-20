from pages.models import Page
from rest_framework import serializers

class PageListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = ('name', 'slug')


class PageDetailSerializer(PageListSerializer):
    class Meta(PageListSerializer.Meta):
        fields = ('name', 'slug', 'content')
