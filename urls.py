from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('apps.main.urls', namespace="main")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('apps.api.urls')),
)

from django.conf import settings

urlpatterns += patterns('',
   (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
