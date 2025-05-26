from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),

    path('usuario/', include('app_prueba.urls')),

    path('inventario/', include('app_inventario.urls')),


]
