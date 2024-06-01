from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, CreateView, DeleteView, UpdateView)
from django.views.generic.detail import DetailView
from fittechnology.settings import LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from .models import Clasificacion, DatosPersona
from .forms import ClasificacionForm, DatosPersonaForm, DatosPersonaFilterForm


@login_required(login_url=LOGOUT_REDIRECT_URL)
def gestionindex(request):

    context = {
        'username': request.user.username
    }
    return render(request, 'gestion/index.html', context)


class ListClasificacion(ListView):
    model = Clasificacion
    paginate_by = 16
    queryset = Clasificacion.objects.all().order_by('codigo')

    @method_decorator(login_required(login_url=LOGOUT_REDIRECT_URL))
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('gestion.view_clasificacion'):
            return redirect(LOGIN_REDIRECT_URL)
        return super(ListClasificacion, self).dispatch(request, *args, **kwargs)


class AddClasificacion(CreateView):
    model = Clasificacion
    form_class = ClasificacionForm
    success_url = reverse_lazy("grados-list")

    @method_decorator(login_required(login_url=LOGOUT_REDIRECT_URL))
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('gestion.add_clasificacion'):
            return redirect(LOGIN_REDIRECT_URL)
        return super(AddClasificacion, self).dispatch(request, *args, **kwargs)


class DeleteClasificacion(DeleteView):
    model = Clasificacion
    success_url = reverse_lazy("grados-list")

    @method_decorator(login_required(login_url=LOGOUT_REDIRECT_URL))
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('gestion.delete_clasificacion'):
            return redirect(LOGIN_REDIRECT_URL)
        return super(DeleteClasificacion, self).dispatch(request, *args, **kwargs)


class EditClasificacion(UpdateView):
    model = Clasificacion
    form_class = ClasificacionForm
    success_url = reverse_lazy("grados-list")

    @method_decorator(login_required(login_url=LOGOUT_REDIRECT_URL))
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('gestion.change_clasificacion'):
            return redirect(LOGIN_REDIRECT_URL)
        return super(EditClasificacion, self).dispatch(request, *args, **kwargs)


class ListDatosPersona(TemplateView):
    template_name = 'gestion/datopersona_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['datospersona'] = DatosPersona.objects.filter(user=self.request.user.id)
        context['username'] = self.request.user.username
        return context


class AddDatoPersona(CreateView):
    model = DatosPersona
    form_class = DatosPersonaForm
    success_url = reverse_lazy("datopersona-detalle")

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        form.instance.clasificacion_id = 17
        return super(AddDatoPersona, self).form_valid(form)


class EditDatoPersona(UpdateView):
    model = DatosPersona
    form_class = DatosPersonaForm
    success_url = reverse_lazy("datopersona-detalle")

    @method_decorator(login_required(login_url=LOGOUT_REDIRECT_URL))
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('gestion.change_datospersona'):
            return redirect(LOGIN_REDIRECT_URL)
        return super(EditDatoPersona, self).dispatch(request, *args, **kwargs)


class ListDatoPersonaCurso(ListView):
    model = DatosPersona
    template_name = 'gestion/cursopersona_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_clas'] = self.kwargs.get('id_clas')
        return context

    def get_queryset(self):
        id_clas = self.kwargs.get('id_clas')
        return DatosPersona.objects.filter(clasificacion=id_clas)


class EditDatoPersonaCurso(UpdateView):
    model = DatosPersona
    form_class = DatosPersonaFilterForm
    template_name = 'gestion/cursopersona_form.html'
    success_url = reverse_lazy("grados-list")

    @method_decorator(login_required(login_url=LOGOUT_REDIRECT_URL))
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('gestion.change_datospersona'):
            return redirect(LOGIN_REDIRECT_URL)
        return super(EditDatoPersonaCurso, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_clas'] = self.kwargs.get('id_clas')
        return context


class EstudianteDetail(TemplateView):
    template_name = 'gestion/estudiante_detalle.html'

    @method_decorator(login_required(login_url=LOGOUT_REDIRECT_URL))
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('gestion.view_datospersona'):
            return redirect(LOGIN_REDIRECT_URL)
        return super(EstudianteDetail, self).dispatch(request, *args, **kwargs)


class DocenteDetail(TemplateView):
    template_name = 'gestion/docente_detalle.html'

    @method_decorator(login_required(login_url=LOGOUT_REDIRECT_URL))
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('gestion.view_datospersona'):
            return redirect(LOGIN_REDIRECT_URL)
        return super(DocenteDetail, self).dispatch(request, *args, **kwargs)
