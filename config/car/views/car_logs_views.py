from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.db import connection
import os
from datetime import datetime
import pandas as pd
import pyodbc
import openpyxl


class LogView(View):
        
        def get(self, request):
            os.system("cls")
            with connection.cursor() as cursor:
                cursor.execute(
                    "select * from log.cars",
                    )
                result = cursor.fetchall()
                logs = []
                for row in result:
                    columns = [col[0] for col in cursor.description]
                    car_dict = {columns[i]: row[i] for i in range(len(columns))}
                    logs.append(car_dict)
            print(logs)
            return render(request, 'logs.html', {
                "logs": logs
            })
    
        def post(self, request):
            os.system("cls")
            car_id = self.request.POST.get('car_id')
            print(car_id)
            with connection.cursor() as cursor:
                cursor.execute(f"UPDATE dbo.cars SET deleted = 0 WHERE id ={car_id};")
                cursor.commit()
            return redirect("car_list")