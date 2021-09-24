from django.urls import path

from . import views

urlpatterns = [

    path('',views.taskview,name='result'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/',views.update,name='update')

]