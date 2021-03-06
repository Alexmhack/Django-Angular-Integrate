from rest_framework import routers

from .viewsets import BlogViewSet

app_name = 'blogs-router'

router = routers.SimpleRouter()

router.register('', BlogViewSet)

urlpatterns = router.urls
