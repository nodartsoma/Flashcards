from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import FlashCard
from .forms import FlashCardForm



class CardListView(ListView):
    model = FlashCard
    template_name = 'cards/card_list.html'
    context_object_name = 'cards'


class CardCreateView(CreateView):
    model = FlashCard
    form_class = FlashCardForm
    template_name = 'cards/add_card.html'
    success_url = reverse_lazy('card_list')


class CardUpdateView(UpdateView):
    model = FlashCard
    form_class = FlashCardForm
    template_name = 'cards/update_card.html'
    success_url = reverse_lazy('card_list')


class CardDeleteView(DeleteView):
    model = FlashCard
    template_name = 'cards/card_confirm_deletion.html'
    success_url = reverse_lazy('card_list')


