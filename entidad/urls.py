from django.urls import path

from . import views

urlpatterns = [
    path('', views.hospitales, name='hospitales'),
    path('create/', views.create, name='create'),
    path('detail/<slug:post_slug>', views.read, name='detail'),
    path('delete/<int:post_id>', views.delete, name='delete'),
    path('update/<int:post_id>', views.update, name='update')

]