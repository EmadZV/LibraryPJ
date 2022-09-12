from django.db import models


# class Price(models.Model):
#     price = models.PositiveIntegerField()
#     discount = models.DecimalField(max_digits=2, decimal_places=2)
#
#     def __str__(self):
#         return str(self.price)


class Debt(models.Model):
    user = models.ForeignKey('myauth.MyUser', on_delete=models.CASCADE, null=True)
    # price = models.OneToOneField(Book.price, on_delete=models.CASCADE, null=True)


class Loan(models.Model):
    user = models.ForeignKey('myauth.MyUser', on_delete=models.CASCADE, null=True)