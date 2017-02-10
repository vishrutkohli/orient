from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'linkedin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^linkedin/$', 'api.views.index', name='home'),
    url(r'^return_data$', 'api.views.return_data', name='return_data'),
    url(r'^autocall$', 'api.views.autocall', name='autocall'),
#    url(r'^saved$', 'api.views.saved2', name='saved2'),
    url(r'^login_orient$', 'api.views.login_orient', name='login_orient'),
    url(r'^update_data$', 'api.views.update_data', name='update_data'),


    # url(r'^info$', 'api.views.api', name='home'),
)
