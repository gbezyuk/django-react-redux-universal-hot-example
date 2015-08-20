from rest_framework import routers
from .viewsets import CategoryViewSet, PhotoViewSet, PageViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'pages', PageViewSet)
