from predictor.forms import MyForm
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from datetime import datetime, time, date   

class inputForm(forms.Form):
  plate = forms.CharField(label="Plate number")
  date = forms.DateTimeField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateTimeInput(attrs={
            'type':'date'
        })
    )
       
  time = forms.DateTimeField(
        label='Time Field', label_suffix=" : ",
        required=True, input_formats=["%H:%M"],
        error_messages={'required': "This field is required."},
        widget=forms.DateTimeInput(attrs={
            'type':'time'
        })
    )



def home(request): 
  form = inputForm(request.POST) 
  #rendering the home templte
  return render(request, 'plate.html',{'form': inputForm})


def vehiculePlate(plate, datee, timee):
  days = {
  'monday':[1,2],
  'tuesday':[3,4],
  'wednesday':[5,6],
  'thrusday':[7,8],
  'friday':[9,0],
  }

  lastDigit = plate[-1]
  hours = time(13,30,0) 
  # datec = '13/08/2021'

  day, month, year = (int(x) for x in datee.split('/'))    
  ans = date(year, month, day).strftime("%A").lower()

  if ans not in days.keys():
    print(f'YES {plate} YOU CAN DRIVEEE')
  else:
    if ((hours >= time(7,0,0) and hours <= time(9,30,0)) or (hours >= time(16,0,0) and hours <= time(19,30,0))):
      print(f'NOO {plate} YOU CANNOT DRIVE')
    else:  
      print(f'YES {plate} YOU CAN DRIVE')



def check(request):
  if request.method=='POST':
      placa = request.POST['placa']
      date  = request.POST['DateTimeField'] 

      print(placa)
      print(date)
      return HttpResponse(placa)

