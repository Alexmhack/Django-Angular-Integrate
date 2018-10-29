from rest_framework import viewsets
from rest_framework import permissions

from blogs.models import Blog
from .serializers import BlogModelSerializer

class BlogViewSet(viewsets.ModelViewSet):
	queryset = Blog.objects.all()
	serializer_class = BlogModelSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
