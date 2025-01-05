from django.urls import path
from .views import ProductListView  # API view-larni import qilish

urlpatterns = [
    path('languages/', ProductListView.as_view(), name='language-list'),  # Mahsulotlar ro'yxati
]
