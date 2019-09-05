from django.urls import path

from . import views 

urlpatterns = [ 
    path('', views.index, name='index'),
    path('criar/', views.criar, name='criar'),
    path('buscar/', views.buscar, name='buscar'),
    path('novos/', views.novos, name='novos'),
    path('historico/', views.historico, name='historico'),
    path('<int:requerimento_id>/resposta/', views.resposta, name='resposta'),
]