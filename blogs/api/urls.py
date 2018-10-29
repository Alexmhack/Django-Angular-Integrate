from django.urls import path

from .views import BlogCRAPIVIew

app_name = 'blogs-api'

urlpatterns = [
	path('', BlogCRAPIVIew.as_view(), name='list-create'),
]
