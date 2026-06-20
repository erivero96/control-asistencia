from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render


@login_required
def home(request):
    return render(request, 'core/home.html')


class InicioSesionView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            f'Bienvenido, {self.request.user.get_username()}.',
        )
        return response


class CerrarSesionView(LogoutView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        messages.success(request, 'Sesión cerrada correctamente.')
        return response
