from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'face.views.home', name='home'),
    url(r'^img/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+)$', 'face.views.image', name='image'),
    url(r'^exists/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+)$', 'face.views.exists', name='exists'),
    url(r'^test/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+)$', 'face.views.test', name='test'),
    url(r'^api/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+)$', 'face.views.api', name='api'),
    
    # url(r'^mandel/', include('mandel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
