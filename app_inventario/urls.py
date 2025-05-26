from django.urls import path
from .views import(
InventarioRetrieveView,
InventarioCreateView,
InventarioUpdateView,
InventarioDestroyView,
MarcaRetrieveView,
MarcaListCreateView,
MarcaListUpdateView,
MarcaListDestroyView,
CategoriaListRetriveView,
CategoriaListCreateView,
CategoriaListUpdateView,
CategoriaListDestroyView,
EstadoListRetrieveView,
EstadoListCreateView,
EstadoListUpdateView,
EstadoListDestroyView,
)



urlpatterns = [ 
    #---------------------------------
    #Inventario
    #---------------------------------
    
    #GET    -> Obtener un usuario por ID
    #PUT    -> Reemplazar todos los campos del usuario
    #PATCH  -> Actualizar algunos campos del usuario
    #DELETE -> Eliminar un usuario 
    # GET -> Listar todos los usuarios
    # POST -> Crear un nuevo usuario

    path('inventario1/', InventarioCreateView.as_view(), name="InventarioCreateView"),
    path('inventario2/', InventarioRetrieveView.as_view(), name="InventarioRetrieveView"),
    path('inventario3/', InventarioUpdateView.as_view(), name="InventarioUpdateView"),
    path('inventario4/', InventarioDestroyView.as_view(), name="InventarioDestroyView"),

    #---------------------------------
    #Marca
    #---------------------------------
    
    #GET    -> Obtener un usuario por ID
    #PUT    -> Reemplazar todos los campos del usuario
    #PATCH  -> Actualizar algunos campos del usuario
    #DELETE -> Eliminar un usuario 
    # GET -> Listar todos los usuarios
    # POST -> Crear un nuevo usuario
   
    path('marca1/', MarcaListCreateView.as_view(), name="MarcaListCreateView"),
    path('marca2/', MarcaRetrieveView.as_view(), name="MarcaRetrieveView"),
    path('marca3/', MarcaListUpdateView.as_view(), name="MarcaListUpdateView"),
    path('marca4/', MarcaListDestroyView.as_view(), name="MarcaListDestroyView"),

    #---------------------------------
    #Categoria
    #---------------------------------
    
    #GET    -> Obtener un usuario por ID
    #PUT    -> Reemplazar todos los campos del usuario
    #PATCH  -> Actualizar algunos campos del usuario
    #DELETE -> Eliminar un usuario 
    # GET -> Listar todos los usuarios
    # POST -> Crear un nuevo usuario

    path('categoria1/', CategoriaListCreateView.as_view(), name="CategoriaListCreateView"),
    path('categoria2/', CategoriaListRetriveView.as_view(), name="CategoriaListRetriveView"),
    path('categoria3/', CategoriaListUpdateView.as_view(), name="CategoriaListUpdateView"),
    path('categoria4/', CategoriaListDestroyView.as_view(), name="CategoriaListDestroyView"),

    #---------------------------------
    #Estado
    #---------------------------------
    
    #GET    -> Obtener un usuario por ID
    #PUT    -> Reemplazar todos los campos del usuario
    #PATCH  -> Actualizar algunos campos del usuario
    #DELETE -> Eliminar un usuario 
    # GET -> Listar todos los usuarios
    # POST -> Crear un nuevo usuario

    path('estado1/', EstadoListCreateView.as_view(), name="EstadoListCreateView"),
    path('estado2/', EstadoListRetrieveView.as_view(), name="EstadoListRetrieveView"),
    path('estado3/', EstadoListUpdateView.as_view(), name="EstadoListUpdateView"),
    path('estado4/', EstadoListDestroyView.as_view(), name="EstadoListDestroyView"),


]

