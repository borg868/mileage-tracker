from django import forms
import datetime

class EntryForm(forms.Form):
    date = forms.DateField(initial=datetime.date.today)
    odometer = forms.IntegerField()
    gallons = forms.DecimalField(decimal_places=3, max_digits=5)
    price = forms.DecimalField(decimal_places=2, max_digits=5)