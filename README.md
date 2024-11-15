# Ex02 Django ORM Web Application
## Date: 15/11/2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![Screenshot 2024-11-15 200429](https://github.com/user-attachments/assets/6a3514d2-dcee-454e-b6cb-801286b01da4)


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

models.py
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
admin.py
```
from django.contrib import admin
from .models import BankLoan,BankLoanAdmin
admin.site.register(BankLoan,BankLoanAdmin)
```

## OUTPUT

![Screenshot 2024-11-15 222740](https://github.com/user-attachments/assets/a4fdfb32-44a9-4b7b-bcf8-6034d7b8a60f)

![Screenshot 2024-11-15 224020](https://github.com/user-attachments/assets/664f4ed6-e72a-4dcc-82cf-f20d762faeeb)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
