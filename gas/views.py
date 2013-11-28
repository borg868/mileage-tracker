from django.shortcuts import render
from gas.models import User, Fillup

# Create your views here.
def entry(request):
    
    context = {' '}
    return render(request, 'gas/entry.html', context)
