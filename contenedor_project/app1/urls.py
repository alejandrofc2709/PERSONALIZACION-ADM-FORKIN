from django.urls import path
from .views import saludoView, indexView


urlpatterns = [
    path('', indexView),
    path('saludo/<str:nombre>/', saludoView),
]
