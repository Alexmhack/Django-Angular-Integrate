from django.contrib import admin

from .models import Blog

@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
	list_display = ('owner', 'title', 'timestamp')
	search_fields = ('owner', 'title', 'content')
	list_filter = ('owner',)
	list_editable = ('title',)
