import django_filters
from .models import Flashcard
from django_filters import DateFilter


class OrderFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date_created", lookup_expr="gte")

	class Meta:
		model = Flashcard
		fields = ['front_native', 'back_translation', 'category']
