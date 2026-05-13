from django import forms

from .models import Employee, Customer


class EmployeeForm(forms.ModelForm):

    class Meta:

        model = Employee

        fields = '__all__'

        widgets = {

            'joining_date': forms.DateInput(attrs={'type': 'date'}),

        }


class CustomerForm(forms.ModelForm):

    class Meta:

        model = Customer

        fields = '__all__'

        widgets = {

            'deadline_of_pay': forms.DateInput(attrs={'type': 'date'}),

        }