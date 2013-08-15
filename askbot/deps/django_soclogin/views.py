from __future__ import absolute_import
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _
from django.contrib.auth import logout


class SocialAuthSigninView(TemplateView):
    template_name = 'django_soclogin/assoc_list.html'


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)
