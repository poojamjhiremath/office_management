from django import forms
from .models import Employee, Customer

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'