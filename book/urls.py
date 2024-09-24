from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('hello/', views.hello_world_view, name="hello"),
    path('post/', views.post_view, name="post"),
]
