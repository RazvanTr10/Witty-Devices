from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path(
        'comment/<int:comment_id>/delete/',
        views.delete_comment, name='delete_comment'),
]
