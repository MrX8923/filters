from django import forms
from .models import *


class MovieChooseForm(forms.Form):
    year_from_table: list[tuple[str, str]] = \
        sorted(set([(str(movie.year),  str(movie.year)) for movie in MovieModel.objects.all()] + [('all', 'Все')]),
               reverse=True)
    country_from_table = \
        sorted(set([(str(movie.country),  str(movie.country)) for movie in MovieModel.objects.all()]
                   + [('all', 'Все')]))
    year = forms.TypedChoiceField(
        label='Выбрать год',
        choices=year_from_table
    )
    country = forms.TypedChoiceField(
        label='Выбрать страну',
        choices=country_from_table
    )
    filter_mark = forms.BooleanField(
        label='Не выводить год',
        required=False
    )


