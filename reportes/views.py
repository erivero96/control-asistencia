from django.shortcuts import render


def panel_reportes(request):
    """Muestra las opciones iniciales del módulo de reportes."""
    return render(request, 'reportes/panel_reportes.html')
