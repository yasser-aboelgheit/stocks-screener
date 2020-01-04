from django.urls import path
from .views import StockAPIView

urlpatterns = [
    path('', StockAPIView.as_view(),name = "company_list"),
]