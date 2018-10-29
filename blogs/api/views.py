from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.decorators import action

from blogs.models import Blog
from .serializers import BlogModelSerializer

class BlogListCreateAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	serializer_class = BlogModelSerializer
	permission_classes = (permissions.IsAuthenticated,)

	def get_queryset(self):
		qs = Blog.objects.all()
		queryset = qs.filter(owner=self.request.user)
		return queryset

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

	# adds the post method in allowed methods list
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


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


class BlogRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = BlogModelSerializer
	permission_classes = (permissions.IsAuthenticated,)

	def get_queryset(self):
		qs = Blog.objects.filter(owner=self.request.user)
		return qs
