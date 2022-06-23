from django.forms import ModelForm
from .models import NeighborHood

class NeighborHoodForm(ModelForm):
    class Meta:
        model = NeighborHood
        fields = '__all__'
        exclude = [ 'user' ]