from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from timer.views import hello, current_datetime, hours_ahead
from djangoclass.views import home

urlpatterns = patterns('',
	# Examples:
	url(r'^hello/$', hello, name="hello"),
	url(r'^time/$', current_datetime, name="timer"),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead, name="timerplus"),
	url(r'^home/$', home, name="home"),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
	url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
    # url(r'^djangoclass/', include('djangoclass.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
        url(r'^admin/', include(admin.site.urls)),

)
