from rest_framework import routers

from .viewsets import BlogViewSet

router = routers.SimpleRouter()

router.register('', BlogViewSet, basename='list')

urlpatterns = router.urls
