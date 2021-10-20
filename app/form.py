from django.forms import ModelForm
from app.models import Carro


# Create the form class.
class CarroForm(ModelForm):
     class Meta:
         model = Carro
         fields = ['modelo', 'marca', 'ano', 'preco']
