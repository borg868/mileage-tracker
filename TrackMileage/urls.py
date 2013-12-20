from django.conf.urls import patterns, include, url
from gas import views
from django.contrib import admin
#from gas.models import Fillup
#from django.views.generic import ListView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TrackMileage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   url(r'^admin/', include(admin.site.urls)),
   #url(r'^entry/', views.entry, name='entry'),
   url(r'^entry/', views.FillupEntryView.as_view(), name='entry'),
   url(r'^listing/$', views.FillupListView.as_view(), name='list'),
   url(r'^listing/(?P<user_id>\d+)/$', views.FillupListView.as_view(), name='userlist'),
)
