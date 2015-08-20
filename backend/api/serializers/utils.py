from rest_framework.serializers import ImageField
from django.contrib.sites.shortcuts import get_current_site


# hack to deal with nginx upstream wrong naming
class MyImageField(ImageField):
    def to_representation(self, value):
        if self.use_url:
            if not value:
                return None
            return 'http://' + get_current_site(self.context.get('request', None)).domain + value.url
        return value.name
