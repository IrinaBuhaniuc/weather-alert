from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponseRedirect

# Create your views here.

def add_user(request):
    submitted = False
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_user?submitted = True')
    else:
        form = UserForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'upload.html', {'form' : form, 'submitted': submitted})