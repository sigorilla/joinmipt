from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    url(r'^', include('joinme.urls', namespace="joinme")),

    url(r'^admin/', include(admin.site.urls)),
)

handler404 = 'django_project.views.handler404'
handler500 = 'django_project.views.handler500'
