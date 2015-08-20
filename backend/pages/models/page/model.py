from django.utils.translation import ugettext_lazy as _
from common.mixins import TimeStampMixin, NameSlugMixin, OrderMixin, IsEnabledMixin
from django.db import models


class Page(TimeStampMixin, NameSlugMixin, OrderMixin, IsEnabledMixin):
    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')
        app_label = 'pages'
        default_related_name = 'pages'
        ordering = ('order',)

    content = models.TextField(verbose_name=_('content'))
