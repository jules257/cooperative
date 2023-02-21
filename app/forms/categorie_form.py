from django.forms import ModelForm
from app.models import Categorie

class CategorieForm(ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__'