"""
App URL Configuration. For more information please see:
https://docs.djangoproject.com/en/1.8/topics/http/urls/
"""
from django.conf.urls import include, url
from django.contrib import admin
from api.router import router as api_router
from django.conf.urls.static import static
from django.conf import settings
from filebrowser.sites import site
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api_router.urls)),
    url(r'^$', RedirectView.as_view(url='/api/', permanent=False))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
