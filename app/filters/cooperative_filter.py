import django_filters
from app.models import Cooperative

class CooperativeFilter(django_filters.FilterSet):
    class Meta:
        model = Cooperative
        fields = [
            'categorie'
            ]