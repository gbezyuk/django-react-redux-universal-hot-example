from ordered_model.admin import OrderedModelAdmin


class PageAdmin(OrderedModelAdmin):
    list_display = ('pk', 'name', 'slug', 'is_enabled', 'move_up_down_links', 'order', 'created', 'updated')
    list_display_links = ('pk',)
    list_filter = ('is_enabled',)
    date_hierarchy = 'modified'
    list_editable = ('name', 'slug', 'is_enabled')
