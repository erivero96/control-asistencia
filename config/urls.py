"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.static import serve

urlpatterns = [
    path('', include('core.urls')),
    path('estudiantes/', include('estudiantes.urls')),
    path('academico/', include('academico.urls')),
    path('notas/', include('notas.urls')),
    path('asistencia/', include('asistencia.urls')),
    path('reportes/', include('reportes.urls')),
    path('admin/', admin.site.urls),
]

# Permite servir los recursos visuales locales desde la misma configuración
# usada por el proyecto durante el desarrollo.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
else:
    urlpatterns.append(
        path('static/<path:path>', serve, {'document_root': settings.STATICFILES_DIRS[0]}),
    )
