from rest_framework import serializers

from blogs.models import Blog
from accounts.api.serializers import AccountModelSerializer

class BlogModelSerializer(serializers.ModelSerializer):
	owner = AccountModelSerializer(read_only=True)

	class Meta:
		model = Blog
		fields = ('owner', 'title', 'content', 'timestamp', 'updated')
		read_only_fields = ('user', 'id')

	def get_updated(self, obj):
		if obj.timestamp == obj.updated:
			return None
		return obj.updated.strftime("%b %d, %Y at %H:%M %p")

	def get_timestamp(self, obj):
		return obj.timestamp.strftime("%b %d, %Y at %H:%M %p")
