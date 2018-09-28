from django.contrib import admin
from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('',                views.products_list, name="list"),
    path('create',          views.products_create),
    path('<int:id>/',       views.products_detail, name="detail"),
    path('<int:id>/edit/',  views.products_update, name="update"),
    path('<int:id>/delete/',views.products_delete),
]
