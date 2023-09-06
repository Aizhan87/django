from django.urls import path
from menu import views

urlpatterns = [
    path('<str:dish>', views.menuitems),
    path('form/', views.form_view),
]