from django.shortcuts import render, redirect
from django.views import View
from django.db import connection
import os


class ServiceCreate(View):
    
    def get(self, request):
        os.system("cls")
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC get_sold_cars @user_id=2",
                # [request.user.id]
                )
            result = cursor.fetchall()
            print(result)
            solded_cars = []
            for row in result:
                columns = [col[0] for col in cursor.description]
                car_dict = {columns[i]: row[i] for i in range(len(columns))}
                solded_cars.append(car_dict)
        print(solded_cars)
        return render(request, 'car_service.html', {
            "solded_cars": solded_cars
        })

    def post(self, request):
        os.system("cls")
        service_car_id = request.POST.get('service_model')
        service_type = request.POST.get('service_type')
        service_date = request.POST.get('service_date')
        service_notes = request.POST.get('service_notes') 
        print(service_car_id, service_type, service_date, service_notes)
        with connection.cursor() as cursor:
            cursor.execute("exec dbo.add_service @arac_id=%s, @type='%s, @notes=%s, @date=%s",
                [int(service_car_id), service_type, service_notes, str(service_date)]
            )
            cursor.commit()
        return redirect("service_list")
    

class ServiceList(View):
    def get(self, request):
        os.system("cls")
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC get_services"
                )
            result = cursor.fetchall()
            print(result)
            servisler = []
            if result != None:
                for row in result:
                    columns = [col[0] for col in cursor.description]
                    servis_dict = {columns[i]: row[i] for i in range(len(columns))}
                    servisler.append(servis_dict)
            print(servisler)
        return render(request, 'service_table.html', {
            "servisler": servisler
        })
    
