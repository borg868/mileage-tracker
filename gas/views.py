from django.shortcuts import render
from gas.forms import EntryForm
from gas.models import User, Fillup
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

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
            fillup.user = form.cleaned_data['user']
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

class FillupEntryView(FormView):
    template_name = 'gas/entry.html'
    form_class = EntryForm

class FillupListView(ListView):
    
    model = Fillup

    def get_context_data(self, **kwargs):
        context = super(FillupListView, self).get_context_data(**kwargs)
        for key, value in self.kwargs.iteritems():
            print key, value
        user_id = self.kwargs.get('user_id', 1)
        print 'user_id = ' + user_id
        context['all'] = self.model.objects.filter(user=User.objects.get(id=user_id))
        return context
