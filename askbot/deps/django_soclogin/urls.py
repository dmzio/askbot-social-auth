# -*- coding: utf-8 -*-
from django.conf import settings as django_settings
from django.conf.urls import patterns, url, include
from .views import SocialAuthSigninView, logout_view

if django_settings.ASKBOT_TRANSLATE_URL:
    from django.utils.translation import ugettext as _
else:
    _ = lambda val: val

urlpatterns = patterns('',

     # manage account registration
    url(r'^signin/$', SocialAuthSigninView.as_view(), name='user_signin'),

    url(r'^logout/$', logout_view, name='logout'),
    url(r'', include('social_auth.urls')),
)
