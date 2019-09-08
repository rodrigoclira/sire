from django.urls import path

from . import views 

urlpatterns = [ 
    path('', views.index, name='index'),
    path('criar/', views.RequerimentoFormView.as_view(), name="criar"),
    path('buscar/', views.buscar, name='buscar'),
    path('novos/', views.novos, name='novos'),
    path('historico/', views.historico, name='historico'),
    path('foo/', views.foo, name='foo'),
    path('<int:requerimento_id>/responder/', views.responder, name='responder'),
    path('<int:requerimento_id>/visualizar/', views.editar, name='editar'),
]