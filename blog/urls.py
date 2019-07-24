from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('blog/', views.blog, name= 'blog'),
    path('stats/', views.stats, name= 'stats'),
    path('tasks/newtask/', views.new_task, name = 'new_task'),
    path('edit/<int:id>/', views.edit_task, name = 'edit_task'),

]
