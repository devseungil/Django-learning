
from django.urls import path
from . import views

app_name = 'app1'
urlpatterns = [
    path('index/', views.index, name = 'index'),
    # path('new/', views.new, name = 'new'),
    path('creat/', views.creat, name = 'creat'),
    path('<int:pk>', views.detail , name = 'detail'),
    path('<int:pk>/delete', views.delete , name = 'delete'),
    # path('<int:pk>/edit', views.edit , name = 'edit'),
    path('<int:pk>/update', views.update , name = 'update'),

]