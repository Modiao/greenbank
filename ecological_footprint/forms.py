from django import forms



from .models import InfosVehiculeFoyer


class InfosVehiculeFoyerForm(forms.ModelForm):
    class Meta:
        model = InfosVehiculeFoyer
        fields = ['type_vehicule', 'energy', 'mileage', 'year', 'passenger']