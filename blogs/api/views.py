from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions

from blogs.models import Blog
from .serializers import BlogModelSerializer

class BlogCRAPIVIew(generics.ListAPIView, mixins.CreateModelMixin):
	queryset = Blog
	serializer_class = BlogModelSerializer()
	permission_classes = (permissions.IsAuthenticated,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class BlogListAPIView(generics.ListAPIView):
	serializer_class = BlogModelSerializer

	def get_queryset(self):
		qs = Blog.objects.all().order_by("-timestamp")
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
				Q(content__icontains=query) |
				Q(user__username__icontains=query)
			)
		return qs
