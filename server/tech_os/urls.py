from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('apps.users.urls')),
    path('api/ambientes/', include('apps.ambientes.urls')),
    path('api/patrimonios/', include('apps.patrimonios.urls')),
    path('api/manutentores/', include('apps.manutentores.urls')),
    path('api/gestores/', include('apps.gestores.urls')),
    path('api/ordens-servico/', include('apps.ordens_de_servico.urls')),
    path('api/areas/', include('apps.areas.urls')),
]
