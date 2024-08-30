from django.urls import path
from . import views

urlpatterns = [
    path('', views.balanco_view, name='balanco'),
    path('add-ativo/', views.add_ativo, name='add_ativo'),
    path('add-passivo/', views.add_passivo, name='add_passivo'),
    path('edit_ativo/<int:id>/', views.edit_ativo, name='edit_ativo'),
    path('delete_ativo/<int:id>/', views.delete_ativo, name='delete_ativo'),
    path('edit_passivo/<int:id>/', views.edit_passivo, name='edit_passivo'),
    path('delete_passivo/<int:id>/', views.delete_passivo, name='delete_passivo'),
    path('demonstracao-resultados/', views.demonstracao_resultados, name='demonstracao_resultados'),
    path('add-demonstracao-resultado/', views.add_demonstracao_resultado, name='add_demonstracao_resultado'),
    path('edit_demonstracao_resultado/<int:pk>/', views.edit_demonstracao_resultado, name='edit_demonstracao_resultado'),
    path('delete_demonstracao_resultado/<int:pk>/', views.delete_demonstracao_resultado, name='delete_demonstracao_resultado'),
]