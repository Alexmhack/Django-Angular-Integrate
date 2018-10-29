from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
]

# blogs app urls
urlpatterns += [
    path('', RedirectView.as_view(url='/blogs/'), name='blogs-redirect'),
    path('blogs/', include('blogs.urls', namespace='blogs')),
]
