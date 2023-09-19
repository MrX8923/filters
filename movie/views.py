from django.shortcuts import render
from .forms import *
from .models import *


def index(request):
    data = {'title': 'Главная', 'table_show': False}
    if request.POST:
        form = MovieChooseForm(request.POST)
        if form.is_valid():
            if request.POST['year'] == 'all' and request.POST['country'] == 'all':
                movies = MovieModel.objects.all()
            else:
                if request.POST.get('filter_mark') is None and request.POST['country'] == 'all':
                    movies = MovieModel.objects.filter(year=request.POST['year'])
                elif request.POST['country'] != 'all' and request.POST.get('filter_mark') is None:
                    movies = MovieModel.objects.filter(country=request.POST['country'], year=request.POST['year'])
                else:
                    movies = MovieModel.objects

            data['table_show'] = True
            data.update({'movies': movies})
    else:
        form = MovieChooseForm()
    data.update({'form': form})
    return render(request, 'index.html', context=data)
