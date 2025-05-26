from django.urls import path
from .views import(
UsuariosListRetriveView,
UsuariosListCreateView,
UsuariosListUpdateView,
UsuariosListDestroyView,
ClienteListRetrieveView,
ClienteListCreateView,
ClienteListUpdateView,
ClienteListDestroyView,
)

#el urls se encarga de linkear las tablas con la pagina pricipal

urlpatterns = [ 
    #---------------------------------
    #USUARIOS
    #---------------------------------

    path('usuario1/', UsuariosListCreateView.as_view(), name="UsuariosListCreateView"),
    path('usuario2/', UsuariosListRetriveView.as_view(), name="UsuariosListRetriveView"),
    path('usuario3/', UsuariosListUpdateView.as_view(), name="UsuariosListUpdateView"),
    path('usuario4/', UsuariosListDestroyView.as_view(), name="UsuariosListDestroyView"),
   
    #GET    -> Obtener un usuario por ID
    #PUT    -> Reemplazar todos los campos del usuario
    #PATCH  -> Actualizar algunos campos del usuario
    #DELETE -> Eliminar un usuario 

    #---------------------------------
    #CLIENTES
    #--------------------------------
    path('cliente1/', ClienteListCreateView.as_view(), name="ClienteListCreateView"),
    path('cliente2/', ClienteListRetrieveView.as_view(), name="ClienteListRetrieveView"),
    path('cliente3/', ClienteListUpdateView.as_view(), name="ClienteListUpdateView"),
    path('cliente4/', UsuariosListDestroyView.as_view(), name="UsuariosListDestroyView"),
    #GET    -> Obtener un usuario por ID
    #PUT    -> Reemplazar todos los campos del usuario
    #PATCH  -> Actualizar algunos campos del usuario
    #DELETE -> Eliminar un cliente



]

