from django.urls import path
from . import views

urlpatterns = [

    path('', views.login_view, name='login'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('logout/', views.logout_view, name='logout'),

    # Employees

    path('employees/', views.employee_list, name='employee_list'),

    path('employees/create/', views.employee_create, name='employee_create'),

    path('employees/update/<int:pk>/', views.employee_update, name='employee_update'),

    path('employees/delete/<int:pk>/', views.employee_delete, name='employee_delete'),

    # Customers

    path('customers/', views.customer_list, name='customer_list'),

    path('customers/create/', views.customer_create, name='customer_create'),

    path('customers/update/<int:pk>/', views.customer_update, name='customer_update'),

    path('customers/delete/<int:pk>/', views.customer_delete, name='customer_delete'),
]