from django.conf.urls import patterns, include, url
from thxyew_note.views import index, write_note, submit_note, single_note
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thxyew.views.home', name='home'),
    # url(r'^thxyew/', include('thxyew.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', index),
    url(r'^write-note', write_note),
    url(r'^submit-note', submit_note),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^notes/(\d{1,3})/$', single_note),
)