from django.utils.translation import ugettext_lazy as _
from grappelli.dashboard import modules, Dashboard

class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard, see django-grappelli documentation for details
    """
    def init_with_context(self, context):

        self.children.append(modules.AppList(
            _('Content Management'),
            column=1,
            collapsible=False,
            models=('pages.*', 'photos.*'),
        ))

        self.children.append(modules.AppList(
            _('Access Administration'),
            column=1,
            collapsible=False,
            models=('django.contrib.auth.*',),
        ))

        self.children.append(modules.LinkList(
            _('Media Management'),
            column=2,
            collapsible=True,
            children=[
                {
                    'title': _('FileBrowser'),
                    'url': '/admin/filebrowser/browse/',
                    'external': False,
                },
            ]
        ))

        self.children.append(modules.AppList(
            _('Other'),
            column=1,
            collapsible=False,
            models=('django.contrib.sites.*',),
        ))

        self.children.append(modules.LinkList(
            _('Tech Support'),
            column=3,
            collapsible=True,
            children=[
                {
                    'title': _('Original Example Repository'),
                    'url': 'https://github.com/gbezyuk/django-react-redux-universal-hot-example',
                    'external': True,
                },
                {
                    'title': _('Django Framework Site'),
                    'url': 'https://djangoproject.com',
                    'external': True,
                },
                {
                    'title': _('Grigoriy Beziuk'),
                    'url': 'http://vk.com/id85082',
                    'external': True,
                },
            ]
        ))

        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=True,
            column=2,
        ))
