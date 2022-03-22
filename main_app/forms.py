from django.forms import ModelForm, ModelChoiceField
from django import forms
from .models import Gig, Venue

class GigForm(ModelForm):
    venue = forms.ModelChoiceField(queryset = Venue.objects.all())
    class Meta:
        model = Gig
        fields = ('date','venue')
