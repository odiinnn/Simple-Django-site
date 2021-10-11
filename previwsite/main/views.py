from django.shortcuts import render, redirect
from .models import Registration
from .forms import RegForm


def index(request):
    return render(request, 'main.html')


def join(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('home')
        else:
            print('aoihjfoahfofj')
    form = RegForm()
    context = {
        'form': form
    }

    return render(request, 'join.html', context)