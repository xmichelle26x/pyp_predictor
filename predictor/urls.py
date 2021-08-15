from django.urls import path
from predictor import views

urlpatterns = [ 
  path('', views.check, name="check"),
]