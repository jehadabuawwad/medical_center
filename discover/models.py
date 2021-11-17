from django.db import models

# Create your models here.

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
    
    name=models.CharField(max_length=55,default=None)
    email=models.CharField(max_length=55,default=None)
    mobile=models.IntegerField(default=None)
    
    age=models.IntegerField(default=None)
    bmi=models.IntegerField(default=None) 
    avg_glucose_level=models.IntegerField(default=None)    
    gender = models.CharField(max_length=6,choices=GENDER,default=G1)
    ever_married=models.CharField(max_length=5,choices=MARRIED,default=A1)
    hypertension= models.CharField(max_length=5,choices=HYPERTENSION,default=A1)
    work= models.CharField(max_length=32,choices=WORK,default=W2)
