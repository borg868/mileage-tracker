from django.shortcuts import render
from gas.forms import EntryForm
from gas.models import User, Fillup

'''
Entry form to input data.
It is hard-coded to store fill-ups for user 'dummy' (id=1) and octane rating 87.
After successfully posting data, it returns to itself with a confirmation message at the top.
'''
def entry(request):
    context = {}
    
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            fillup = Fillup()
            fillup.user = User.objects.get(username='dummy')
            fillup.purchase_date = form.cleaned_data['date']
            fillup.odometer = form.cleaned_data['odometer']
            fillup.gallons = form.cleaned_data['gallons']
            fillup.price = form.cleaned_data['price']
            fillup.octane_rating = 87
            fillup.save()
            context['flag'] = True
    else:
        form = EntryForm()
        context['flag'] = False

    context['form'] = form
    return render(request, 'gas/entry.html', context)

def list(request):
    
    return render(request, 'gas/list.html', context)
