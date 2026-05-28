from django import forms
from .models import Curs

class CursForm(forms.ModelForm):
    class Meta:
        model = Curs
        fields = ['denumire', 'numar_credite', 'student']

    def clean_numar_credite(self):
        credite = self.cleaned_data['numar_credite']
        if credite < 1 or credite > 10:
            raise forms.ValidationError("nr de credite trb sa fie intre 1 si 10")
        return credite

    def clean_denumire(self):
        denumire = self.cleaned_data['denumire']
        if Curs.objects.filter(denumire=denumire).exists():
            raise forms.ValidationError("exista deja acest curs")
        return denumire