from ordered_model.admin import OrderedModelAdmin
from ..photo.admin import PhotoInline


class CategoryAdmin(OrderedModelAdmin):
    list_display = ('pk', 'name', 'slug', 'is_enabled', 'move_up_down_links', 'order', 'created', 'updated')
    list_display_links = ('pk',)
    list_editable = ('name', 'slug', 'is_enabled')
    list_filter = ('is_enabled',)
    date_hierarchy = 'modified'
    inlines = (PhotoInline,)
