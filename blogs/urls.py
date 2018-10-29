from django.urls import path, include

app_name = 'blogs'

urlpatterns = [
	path('api/', include('blogs.api.urls', namespace='blogs-api')),
]
