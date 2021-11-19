from django.db import models
from django.contrib.auth import get_user_model

class Malady(models.Model):

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
    
    name=models.CharField(max_length=55,default=None,null=True)
    email=models.CharField(max_length=55,default=None,null=True)
    mobile=models.IntegerField(default=None,null=True)
    age=models.IntegerField(default=None,null=True)
    bmi=models.IntegerField(default=None,null=True) 
    avg_glucose_level=models.IntegerField(default=None,null=True)    
    gender = models.CharField(max_length=6,choices=GENDER,default=G1,null=True)
    ever_married=models.CharField(max_length=5,choices=MARRIED,default=A1,null=True)
    hypertension= models.CharField(max_length=5,choices=HYPERTENSION,default=A1,null=True)
    work= models.CharField(max_length=32,choices=WORK,default=W2,null=True)