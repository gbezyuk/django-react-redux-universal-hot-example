from django.db import models
from django.utils.translation import ugettext_lazy as _
from common.mixins import TimeStampMixin, NameSlugMixin, OrderMixin, IsEnabledMixin
from ..category import Category
from filebrowser.fields import FileBrowseField


class Photo(TimeStampMixin, NameSlugMixin, OrderMixin, IsEnabledMixin):
    class Meta:
        verbose_name = _('photo')
        verbose_name_plural = _('photos')
        app_label = 'photos'
        default_related_name = 'photos'
        ordering = ('order',)

    image = FileBrowseField(verbose_name=_('image'), directory='photos/', extensions=[".jpg", ".png"], max_length=500)
    categories = models.ManyToManyField(to=Category, verbose_name=_('category'))
