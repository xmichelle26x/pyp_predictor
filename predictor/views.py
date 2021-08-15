from django.shortcuts import render 
from django import forms
from datetime import datetime, time, date  


#form
class inputForm(forms.Form):
  plate = forms.CharField(label="Plate number")
  plate.widget.attrs.update({'id' : 'plateid'})

  date = forms.DateTimeField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateTimeInput(attrs={
            'type':'date'
        })
    )
  date.widget.attrs.update({'id' : 'plateid'})
       
  time = forms.DateTimeField(
        required=True, input_formats=["%H:%M"],
        error_messages={'required': "This field is required."},
        widget=forms.DateTimeInput(attrs={
            'type':'time'
        })
    )
  time.widget.attrs.update({'id' : 'timeid'})


#validate plate function 
def validatePlate(plate, idate, itime):
  days = {
  1:[1,2],
  2:[3,4],
  3:[5,6],
  4:[7,8],
  5:[9,0],
  } 
  #last digit of the plate
  lastDigit = plate[-1]
  
  #get time from the timepicker
  time2 = datetime.strptime(itime,'%H:%M').time()

  #get date from the datepicker
  day, month, year = (int(float(x)) for x in idate.split('-'))    
  weekday = date(day, month, year).isoweekday()

  #validate the 3 possible scenarios
  if weekday not in days.keys() or int(lastDigit) not in days[weekday]:
    return 1, f'PLATE NUMBER: {plate}, YOU ARE ALLOWED TO DRIVE' 

  if ((time2 >= time(7,0,0) and time2 <= time(9,30,0)) or (time2 >= time(16,0,0) and time2 <= time(19,30,0))):
     return 0, f'PLATE NUMBER: {plate} YOU ARE NOT ALLOWED TO DRIVE'
  else:  
     return 1,  f'PLATE NUMBER: {plate}, YOU ARE ALLOWED TO DRIVE'
  
 
  


def check(request):
  if request.method == 'POST':
      plate = request.POST['plate']
      date  = request.POST['date'] 
      time  = request.POST['time'] 
      res, resp = validatePlate(plate, date, time)
      return render(request,'plate.html', {'form': inputForm, 'res':res, 'resp':resp}) 

  return render(request,'plate.html', {'form': inputForm}) 

