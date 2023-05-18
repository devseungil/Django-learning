from . import views
from django.urls import path

app_name = 'app1'
urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('create/', views.create, name = 'create'),
    path('<int:pk>', views.detail, name = 'detail'),
    path('<int:pk>/update', views.update, name = 'update'),
    path('<int:pk>/delete', views.delete, name = 'delete'),
]