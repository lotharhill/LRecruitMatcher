from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^matcher/', include('matcher.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^', include('matcher.urls')),
]