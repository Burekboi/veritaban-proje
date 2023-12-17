from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views import View
from django.db import connection
from django.http import JsonResponse
import os
from django.contrib.auth import authenticate, login
from car.views.car_views import CarList


class UserCreateView(View):
    def post(self,request):
        with connection.cursor() as cursor:
            cursor.execute(
                """EXEC add_user
                @name=%s,
                @surname=%s,
                @username=%s,
                @password=%s
                """,
                [
                    request.POST.get('register-firstname'),
                    request.POST.get('register-surname'),
                    request.POST.get('register-username'),
                    request.POST.get('register-password')
                ]

                )
            cursor.commit()
        return redirect("login")


def login(request):
    if request.method == "GET":
        return render(request, 'login.html', {"user": []})
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute(
                """EXEC dbo.login
                @username=%s,
                @password=%s
                """,
                [
                    request.POST.get('username'),
                    request.POST.get('password')
                ]

                )
            result = cursor.fetchone()
            if result:
                columns = [col[0] for col in cursor.description]
                user_dict = {columns[i]: result[i] for i in range(min(len(columns), len(result)))}
                users = [user_dict]
                
                print(users[0])

                car_list_view = CarList()
                # return car_list_view.get(request=request, user=users)
                return render(request, 'login.html', {
                    'user': users[0]
                })
            else:
                return render(request, "login.html", {'error_message': 'Invalid login credentials'})



