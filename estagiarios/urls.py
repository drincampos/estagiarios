from django.urls import path
from estagiarios.views import index

urlpatterns = [
    path('', index, name='index')
]