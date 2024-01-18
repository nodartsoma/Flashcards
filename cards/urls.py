from django.urls import path
from . import views

urlpatterns = [
    path('', views.CardListView.as_view(), name="card_list"),
    path('<int:pk>/', views.CardSingletonView.as_view(), name="card_list"),
]
