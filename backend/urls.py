from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]

# blogs app urls
urlpatterns += [
    path('blogs/', include('blogs.urls', namespace='blogs')),
]
