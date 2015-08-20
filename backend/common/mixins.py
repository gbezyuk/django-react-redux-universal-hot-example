from django.db import models
from ordered_model.models import OrderedModel
from model_utils.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _


class TimeStampMixin(TimeStampedModel):
    class Meta:
        abstract = True
    #
    # created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True)
    # updated = models.DateTimeField(verbose_name=_('updated'), auto_now=True)
    @property
    def updated(self):
        return self.modified


class NameSlugMixin(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(verbose_name=_('name'), max_length=255)
    slug = models.SlugField(verbose_name=_('slug'), max_length=40, unique=True)

    def __str__(self):
        return self.name


class IsEnabledMixin(models.Model):
    class Meta:
        abstract = True

    is_enabled = models.BooleanField(verbose_name=_('is enabled'), default=True)

    # enabled = models.Manager
    # disabled = models.Manager
    # TODO: implement objects manager so only enabled entities will be shown via API


class OrderMixin(OrderedModel):
    class Meta(OrderedModel.Meta):
        abstract = True
