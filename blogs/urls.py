from django.urls import path, include

from .views import index_view

app_name = 'blogs'

urlpatterns = [
	path('api/', include('blogs.api.urls', namespace='blogs-api')),
	path('', index_view, name='index'),
]
