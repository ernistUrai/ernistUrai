from django.urls import path
from . import views


urlpatterns = [
    path('phone_list/', views.phone_list_view, name="phone_list"),
    path('phone_list/<int:id>/', views.phone_detail_view, name="phone_detail"),
    path('create_phone/', views.create_phone_view, name="create"),
    path('phone_list/<int:id/update/', views.update_object_view, name="phone_update"),
]