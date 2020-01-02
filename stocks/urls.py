from django.urls import path
from .views import HomeView, GraphView

urlpatterns = [
    path('', HomeView.as_view(),name = "index"),
    path('graph/<str:slug>',GraphView,name="graph"),
]