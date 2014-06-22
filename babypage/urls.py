from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'babypage.views.home', name='home'),
    url(r'^accounts/profile/', 'babypage.views.profile', name='profile'),
)
