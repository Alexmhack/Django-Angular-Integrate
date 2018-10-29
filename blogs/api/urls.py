from django.urls import path

from .views import BlogListCreateAPIView, BlogListAPIView

app_name = 'blogs-api'

urlpatterns = [
	path('', BlogListCreateAPIView.as_view(), name='list-create'),
	path('list/', BlogListAPIView.as_view(), name='list'),
]
