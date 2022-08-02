from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("clenove", views.seznam, name="seznam"),
    path("clenove/<str:prezdivka>", views.detail, name="detail")
]


