from django.urls import path

from . import views

app_name = 'containers'
urlpatterns = [
    path('', views.index, name='index'),
    path('<id>/details/', views.detail, name='detail'),
    path('create/new/', views.create, name='create'),
    path('<id>/start/', views.start, name='start'),
    path('<id>/stop/', views.stop, name='stop'),
    path('<id>/kill/', views.kill, name='kill'),
    path('<id>/restart/', views.restart, name='restart'),
    path('<id>/pause/', views.pause, name='pause'),
    path('<id>/resume/', views.resume, name='resume'),
    path('<id>/delete/', views.delete, name='delete'),
    path('<id>/logs/', views.logfollow, name='logs'),
]
