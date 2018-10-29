from rest_framework import routers

from .views import BlogListCreateAPIView, BlogListAPIView

router = routers.SimpleRouter()

router.register('', BlogListCreateAPIView, basename='list-create')
router.register('list/', BlogListAPIView, basename='list')

urlpatterns = router.urls
