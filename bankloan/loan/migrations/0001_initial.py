# Generated by Django 5.1.2 on 2024-11-12 13:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BankLoan",
            fields=[
                ("loan_id", models.IntegerField(primary_key=True, serialize=False)),
                ("loan_type", models.CharField(max_length=30)),
                ("loan_amt", models.IntegerField()),
                ("cust_acno", models.IntegerField()),
                ("cust_name", models.CharField(max_length=50)),
            ],
        ),
    ]
