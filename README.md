# Ex02 Django ORM Web Application
## Date: 16/11/2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![alt text](<Screenshot 2024-11-15 200429.png>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
from django.db import models
from django.contrib import admin
class BankLoan (models.Model):
    loan_id=models.IntegerField(primary_key=True)
    loan_type=models.CharField(max_length=30)
    loan_amt=models.IntegerField()
    cust_acno=models.IntegerField()
    cust_name=models.CharField(max_length=50)
   
 
class BankLoanAdmin(admin.ModelAdmin):
    list_display=('loan_id','cust_name','loan_type','loan_amt','cust_acno')

```
```
from django.contrib import admin
from .models import BankLoan,BankLoanAdmin
admin.site.register(BankLoan,BankLoanAdmin)
```


## OUTPUT

![alt text](<Screenshot 2024-11-15 222740.png>) 

![alt text](<Screenshot 2024-11-15 224020.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
