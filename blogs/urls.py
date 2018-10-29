from django.urls import path, include

urlpatters = [
	path('api/', include('blogs.api.urls', namespace='blogs-api')),
]
