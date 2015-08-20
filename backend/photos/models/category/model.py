from django.utils.translation import ugettext_lazy as _
from common.mixins import TimeStampMixin, NameSlugMixin, OrderMixin, IsEnabledMixin


class Category(TimeStampMixin, NameSlugMixin, OrderMixin, IsEnabledMixin):
    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        app_label = 'photos'
        default_related_name = 'categories'
        ordering = ('order',)
