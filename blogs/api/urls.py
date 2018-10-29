from django.urls import path

from .views import (
	BlogListCreateAPIView, BlogListAPIView, BlogRUDAPIView
)

app_name = 'blogs-api'

urlpatterns = [
	path('', BlogListCreateAPIView.as_view(), name='list-create'),
	path('list/', BlogListAPIView.as_view(), name='list'),
	path('<int:pk>/detail/', BlogRUDAPIView.as_view(), name='detail')
]
