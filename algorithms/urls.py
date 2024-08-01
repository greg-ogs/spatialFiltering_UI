from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pid_controller/', views.pid_controller, name='pid_controller'),
    path('ann_controller/', views.ann_controller, name='ann_controller'),
    path('ann_train/', views.ann_train, name='ann_train'),
    path('ann_test/', views.ann_tests, name='ann_test'),
    path('nd_controller/', views.nd_controller, name='nd_controller'),
]
