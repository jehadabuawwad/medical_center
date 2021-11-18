from django import forms

class InputUserInfo(forms.Form):

    G1 = 'Male'
    G2 = 'Female'
    A1='True'
    A2='False'
    S1='unknown'
    S2='formerly_smoked'
    S3='never_smoked'
    S4='smokes'
    W1='govt_job'
    W2='never_worked'
    W3='private'
    W4='self-employed'
    W5='children'

    GENDER = [
        (G1, 'Male'),
        (G2, 'Female'),
    ]
   
    MARRIED = [
        (A1, 'True'),
        (A2, 'False'),
    ]

    HYPERTENSION = [
        (A1, 'True'),
        (A2, 'False'),
    ]
 
    SMOKING = [
        (S1, 'unknown'),
        (S2, 'formerly_smoked'),
        (S3, 'never_smoked'),
        (S4, 'smokes'),
    ]

    WORK = [
        (W1, 'govt_job'),
        (W2, 'never_worked'),
        (W3, 'private'),
        (W4, 'Self-employed'),
        (W4, 'children'),
    ]
    
    name=forms.CharField(max_length=55)
    email=forms.CharField(max_length=55)
    mobile=forms.IntegerField()
    
    age=forms.IntegerField()
    bmi=forms.IntegerField() 
    avg_glucose_level=forms.IntegerField()    

    gender = forms.ChoiceField( choices=[GENDER], required=False)
    ever_married = forms.ChoiceField( choices=[MARRIED], required=False)
    hypertension = forms.ChoiceField( choices=[HYPERTENSION], required=False)
    smoking = forms.ChoiceField( choices=[SMOKING], required=False)
    work = forms.ChoiceField( choices=[WORK], required=False)
    
