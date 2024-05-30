from django.shortcuts import render
from django.views.generic import TemplateView
from fittechnology.settings import LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, render


class GestionIndex(TemplateView):
    template_name = 'gestion/index.html'

    @method_decorator(login_required(login_url=LOGOUT_REDIRECT_URL))
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('sivigila.view_archivo'):
            return redirect(LOGIN_REDIRECT_URL)
        return super(GestionIndex, self).dispatch(request, *args, **kwargs)
