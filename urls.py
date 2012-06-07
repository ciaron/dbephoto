from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('photo.views',
    # Examples:
    # url(r'^$', 'dbe.views.home', name='home'),
    # url(r'^dbe/', include('dbe.foo.urls')),

    url(r"^$", "main"),
    url(r"^(\d+)/$", "album"),
    url(r"^(\d+)/(full|thumbnails|edit)/$", "album"),
    url(r"^image/(\d+)/$", "image"),
    url(r"^update/$", "update"),
    url(r"^search/$", "search"),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    'document_root': settings.MEDIA_ROOT}))

