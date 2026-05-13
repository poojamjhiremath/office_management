from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import Employee, Customer
from .forms import EmployeeForm, CustomerForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    employee_count = Employee.objects.count()
    customer_count = Customer.objects.count()

    context = {
        'employee_count': employee_count,
        'customer_count': customer_count
    }

    return render(request, 'dashboard.html', context)


# EMPLOYEE CRUD

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/list.html', {'employees': employees})


@login_required
def employee_create(request):
    form = EmployeeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('employee_list')

    return render(request, 'employees/form.html', {'form': form})


@login_required
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    form = EmployeeForm(request.POST or None, instance=employee)

    if form.is_valid():
        form.save()
        return redirect('employee_list')

    return render(request, 'employees/form.html', {'form': form})


@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('employee_list')


# CUSTOMER CRUD

@login_required
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/list.html', {'customers': customers})


@login_required
def customer_create(request):
    form = CustomerForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('customer_list')

    return render(request, 'customers/form.html', {'form': form})


@login_required
def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    form = CustomerForm(request.POST or None, instance=customer)

    if form.is_valid():
        form.save()
        return redirect('customer_list')

    return render(request, 'customers/form.html', {'form': form})


@login_required
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('customer_list')