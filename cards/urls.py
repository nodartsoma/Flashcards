from django.urls import path
from cards.views import CardListView, CardCreateView, CardUpdateView, CardDeleteView

urlpatterns = [
    path('cards/<int:pk>/add/', CardCreateView.as_view(), name="card_list"),
    path('cards/<int:pk>/update/', CardUpdateView.as_view(), name="card_list"),
    path('cards/list/', CardListView.as_view(), name="card_list"),
    path('cards/<int:pk>/delete/', CardDeleteView.as_view(), name="card_delete"),
]
