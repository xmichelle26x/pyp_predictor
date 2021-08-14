from django import forms 
from django.forms import widgets
from django.forms.widgets import DateInput, TimeInput, DateTimeInput
from .models import Vehicle


# class Create(forms.ModelForm):
#             class Meta:
#                 # model = Vehicle
#                 # fields = ('date','time')
                # widgets = {
                #     'date': forms.DateInput(attrs={'type': 'date'}),
                #     'time': forms.TimeInput(attrs={'type': 'time'})

                # }
#                 widgets = {
#                     'date':DateInput(),
#                     'time':TimeInput(),
#                 }

class MyForm(forms.ModelForm):
        model = Vehicle
        fields = ['cons_date']
        widget = {
            'cons_date': DateTimeInput(format='%d/%m/%Y %H:%M', attrs={'type':'datetime-local'}),
        }