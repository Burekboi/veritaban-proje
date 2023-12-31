"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views.car_views import *
from .views.car_service_views import *
from .views.sales_view import *
from .views.car_logs_views import *

urlpatterns = [
    path("", CarList.as_view(), name="car_list"),
    path("create/", CarCreate.as_view(), name="car_create"),
    path("<int:id>/update/", CarUpdate.as_view(),name="car_update"),
    path("<int:id>/delete/", CarDelete.as_view(), name="car_delete"),

    path("service-create/<int:pk>/", ServiceCreate.as_view(), name="service_create"),
    path("service_list/", ServiceList.as_view(), name="service_list"),

    path("sales/", SalesList.as_view(), name="sales_list"),
    path("sales_create/", SalesCreate.as_view(), name="sales_create"),
    path("sales_excel_convert/", ServiceExcelConvert.as_view(), name="sales_excel_convert"),
    path("sales_excel_import/", ServiceExcelImport.as_view(), name="sales_excel_import"),

    path("logs/", LogView.as_view(), name="logs"),
]
