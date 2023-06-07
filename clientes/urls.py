from django.urls import path
from .views import ClienteList, ClienteDetail

urlpatterns = [
    path ('clientes/', ClienteList.as_view(), name ='cliente-list'),
    path ('clientes/<int:pk>/', ClienteDetail.as_view(), name ='cliente-detail')

]