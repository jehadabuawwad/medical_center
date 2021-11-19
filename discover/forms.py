from django import forms
from .models import Malady

class InputUserInfo(forms.Form):

  class Meta:
      model=Malady
      fields=['name',
            'email',
            'mobile',
            'age',
            'bmi',
            'avg_glucose_level',
            'gender',
            'ever_married',
            'hypertension',
            'work'
            ]