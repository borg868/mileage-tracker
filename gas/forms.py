from django import forms

class EntryForm(forms.Form):
    date = forms.DateField()
    odometer = forms.IntegerField()
    gallons = forms.DecimalField(decimal_places=3, max_digits=5)
    price = forms.DecimalField(decimal_places=2, max_digits=5)