from django.urls import path

from . import views 

urlpatterns = [ 
    path('', views.index, name='index'),
    path('criar/', views.create, name='create'),
    path('pesquisar/', views.search, name='search'),
    path('listar/', views.list_req, name='list_req')
]