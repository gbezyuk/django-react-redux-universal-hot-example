from ordered_model.admin import OrderedModelAdmin
from filebrowser.settings import ADMIN_THUMBNAIL
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import StackedInline
from .model import Photo


class PhotoAdmin(OrderedModelAdmin):
    list_display = ('as_rendered',  'is_enabled', 'name', 'slug',
        'move_up_down_links', 'order', 'created', 'updated')
    list_filter = ('is_enabled', 'categories')
    list_editable = ('name', 'slug', 'is_enabled')
    date_hierarchy = 'modified'

    def as_rendered(self, obj):
        if obj.image and obj.image.filetype == "Image":
            image_style = "color: #fff; height: 240px; width: 320px; \
                display: flex; align-items: center; align-content: center; \
                background: left top url('%s') no-repeat; position: relative;" \
                % obj.image.version_generate(ADMIN_THUMBNAIL).url
            span_style = "background: rgba(0, 0, 0, .3); color: #fff; \
                padding: 1em; border-radius: 0 .5em .5em 0;"
            return "<div style=\"%s\"><span style=\"%s\">%s</span></div>" \
                % (image_style, span_style, obj.name)
        else:
            return obj.name
    as_rendered.allow_tags = True
    as_rendered.short_description = _("as rendered")


class PhotoInline(StackedInline):
    model = Photo.categories.through
