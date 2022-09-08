from django.db import models


class Price(models.Model):
    price = models.PositiveIntegerField()
    discount = models.DecimalField(max_digits=2, decimal_places=2)


class Debt(models.Model):
    user = models.ForeignKey('myauth.MyUser', on_delete=models.CASCADE, null=True)
    price = models.OneToOneField(Price, on_delete=models.CASCADE, null=True)


class Loan(models.Model):
    user = models.ForeignKey('myauth.MyUser', on_delete=models.CASCADE, null=True)