from rest_framework import routers

from .views import BlogListCreateAPIView, BlogListAPIView

router = routers.SimpleRouter()

router.register('', BlogListCreateAPIView)
router.register('list/', BlogListAPIView)

urlpatterns = router.urls
