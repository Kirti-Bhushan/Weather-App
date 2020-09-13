from django.forms import ModelForm,TextInput
from weatherapp.models import CityModel

class CityForm(ModelForm):
    class Meta:
        model=CityModel
        fields=['name']
        widgets={'name':TextInput(attrs={'class':'input','placeholder':'City Name'})}
