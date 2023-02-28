from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)


class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(to=User, on_delete=models.PROTECT)


class Contract(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.PROTECT, related_name='contract_client')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    amount = models.FloatField()
    payment_due = models.DateField()
    sales_contact = models.ForeignKey(to=User, on_delete=models.PROTECT, related_name='sales_contract')


class Event(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.PROTECT)
    contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    attendees = models.IntegerField()
    event_date = models.DateField()
    notes = models.TextField(null=True)
    support_contact = models.ForeignKey(to=User, on_delete=models.PROTECT)