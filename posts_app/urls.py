from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('post-create', views.create_post, name='post-create'),
    path('post-detail/<int:id>/', views.post_details, name='post-detail'),
    path('post-update/<int:id>/', views.post_update, name='post-update'),
    path('post-delete/<int:id>/', views.post_delete, name='post-delete'),
]