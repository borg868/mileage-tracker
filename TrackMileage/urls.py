from django.conf.urls import patterns, include, url
from gas import views
from django.contrib import admin
from django.views.generic import list_detail
from gas.models import Fillup

fillup_info = {
    "queryset" : Fillup.objects.all(),
}


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TrackMileage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   url(r'^admin/', include(admin.site.urls)),
   url(r'^entry/', views.entry, name='entry'),
   url(r'^listing/', list_detail.object_list, fillup_info , name='list')
)
