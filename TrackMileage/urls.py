from django.conf.urls import patterns, include, url
from gas import views
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TrackMileage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   url(r'^admin/', include(admin.site.urls)),
   url(r'^entry/', views.entry, name='entry'),
   url(r'^listing/', views.list, name='list')
)
