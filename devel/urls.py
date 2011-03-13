from django.conf.urls.defaults import patterns

urlpatterns = patterns('devel.views',
    (r'^$',          'index'),
    (r'^clock/$',    'clock'),
    (r'^profile/$',  'change_profile'),
    (r'^newuser/$',  'new_user_form'),
    (r'^admin_log/(?P<username>.*)/$','admin_log'),
    (r'^admin_log/$','admin_log'),
)

# vim: set ts=4 sw=4 et: