from django import forms
from gas.models import User
import datetime

class EntryForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all().order_by('username'), empty_label=None)
    date = forms.DateField(initial=datetime.date.today)
    odometer = forms.IntegerField()
    gallons = forms.DecimalField(decimal_places=3, max_digits=5)
    price = forms.DecimalField(decimal_places=2, max_digits=5)