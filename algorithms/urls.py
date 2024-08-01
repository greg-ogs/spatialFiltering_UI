from django.urls import path
from . import views

urlpatterns = [
    path('algorithms/', views.algorithm_selection, name='algorithm_selection'),
    path('pid_controller/', views.pid_controller, name='pid_controller'),
    path('ann_controller/', views.ann_controller, name='ann_controller'),
    path('nd_controller/', views.nd_controller, name='nd_controller'),
]
