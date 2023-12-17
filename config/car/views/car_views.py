from django.shortcuts import render, redirect
from django.views import View
from django.db import connection
from django.http import JsonResponse
import os

class CarList(View):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC get_cars"
                )
            result = cursor.fetchall()
            cars = []
            for row in result:
                columns = [col[0] for col in cursor.description]
                car_dict = {columns[i]: row[i] for i in range(len(columns))}
                cars.append(car_dict)
            cursor.execute(
                "EXEC get_users"
                )
            result = cursor.fetchall()
        return render(request, 'car_list.html', {
            'araclar': cars,
        })
    

class CarCreate(View):
    
    def post(self, request):
        if request.method == 'POST':
            model = request.POST.get('model')
            year = request.POST.get('year')
            price = request.POST.get('price')
            state = request.POST.get('state')
            engine_capacity = request.POST.get('engine_capacity')
            fuel_type = request.POST.get('fuel_type')
            gear_type = request.POST.get('gear_type')
            traction_type = request.POST.get('traction_type')
            horse_power = request.POST.get('horse_power')
            image = request.FILES['image']

        with open("media/" + self.request.FILES['image'].name, 'wb+') as destination:
            for chunk in self.request.FILES['image'].chunks():
                destination.write(chunk)

        with connection.cursor() as cursor:
                cursor.execute(
                    "EXEC add_car @model=%s, @year=%s, @price=%s, @state=%s, @engine_capacity=%s, @fuel_type=%s, @gear_type=%s, @traction_type=%s, @horse_power=%s, @image=%s",
                                [model, year, price, state, engine_capacity, fuel_type, gear_type, traction_type, horse_power, image.name]
                                )
                cursor.commit()
        return redirect("car_list")


class CarUpdate(View):
    def post(self, request,id):
        os.system("cls")
        print(request)
        print(request.POST)
        with connection.cursor() as cursor:
                cursor.execute(
                    "EXEC upd_car @id=%s, @model=%s, @year=%s, @price=%s, @state=%s, @engine_capacity=%s, @fuel_type=%s, @gear_type=%s, @traction_type=%s, @horse_power=%s",
                                [id, request.POST.get('model'), request.POST.get('year'), request.POST.get('price'), request.POST.get('state'), request.POST.get('engine_capacity'), request.POST.get('fuel_type'), request.POST.get('gear_type'), request.POST.get('traction_type'), request.POST.get('horse_power')]
                                )
                cursor.commit()
        return redirect("car_list")
    

class CarDelete(View):

    def post(self, request,id):
        print(id)
        with connection.cursor() as cursor:
                cursor.execute(
                    f"EXEC delete_car @id={id}"
                                )
                cursor.commit()
        return redirect("car_list")