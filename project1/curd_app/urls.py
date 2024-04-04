from django.urls import path

from .views import ElectricView, ShowView, UpdateView, DeleteView

urlpatterns = [
    path("", ElectricView.as_view(), name="info_url"),
    path("show/", ShowView.as_view(), name="show_url"),
    path("update/<int:pk>", UpdateView.as_view(), name="update_url"),
    path("delete/<int:pk>", DeleteView.as_view(), name="delete_url"),
]
