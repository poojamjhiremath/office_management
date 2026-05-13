from django.db import models


class Employee(models.Model):

    name = models.CharField(max_length=100)

    joining_date = models.DateField()

    department = models.CharField(max_length=100)

    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Customer(models.Model):

    customer_name = models.CharField(max_length=100)

    project_name = models.CharField(max_length=200)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)

    balance_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    deadline_of_pay = models.DateField()

    def save(self, *args, **kwargs):

        self.balance_amount = self.total_amount - self.paid_amount

        super().save(*args, **kwargs)

    def __str__(self):
        return self.customer_name