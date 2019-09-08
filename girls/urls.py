from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    path('girl/<int:girl_id>', views.girl, name='girl'),
    path('edit/<int:girl_id>', views.edit, name='edit'),
    path('delete/<int:girl_id>', views.delete, name='delete'),
]