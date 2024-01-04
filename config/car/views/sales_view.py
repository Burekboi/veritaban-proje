from django.shortcuts import render, redirect
from django.views import View
from django.db import connection
import os


class SalesList(View):
    def get(self, request, pk, *args, **kwargs):
        os.system("cls")
        print("pk:", self.kwargs.get('pk'))
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC dbo.get_sold_cars"
                )
            result = cursor.fetchall()
            sales = []
            if result != None:
                for row in result:
                    columns = [col[0] for col in cursor.description]
                    sales_dict = {columns[i]: row[i] for i in range(len(columns))}
                    sales.append(sales_dict)
            # if sales_dict != {}:
            #     cursor.execute(
            #         "EXEC get_user_detail @id=%s",
            #         [sales_dict['user_id']]
            #         )
            #     result = cursor.fetchall()
            # user = []
            # if result != None:
            #     for row in result:
            #         columns = [col[0] for col in cursor.description]
            #         user_dict = {columns[i]: row[i] for i in range(len(columns))}
            #         user.append(user_dict)
            #         sales[0]['user'] = user[0]
                    
            # if sales_dict != {}:
            #     cursor.execute(
            #         "EXEC get_car_detail @id=%s",
            #         [sales_dict['car_id']]
            #         )
            #     result = cursor.fetchall()
            # car = []
            # if result != None:
            #     for row in result:
            #         columns = [col[0] for col in cursor.description]
            #         car_dict = {columns[i]: row[i] for i in range(len(columns))}
            #         car.append(car_dict)
            #         sales[0]['car'] = car[0]
            #     print(sales)        
            print(sales)    
            return render(request, 'sales.html', {
                "sales": sales
            })
            
            


class SalesCreate(View):
    def post(self, request):
        name = request.POST.get('fullName')
        email = request.POST.get('email')
        creditCard = request.POST.get('creditCard')
        user_id = request.POST.get('user_id')
        car_id = request.POST.get('car_id')
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC proc_car_sale @user_id=%s, @car_id=%s",
                [user_id, car_id]
                )
            cursor.commit()
        print(name, email, creditCard, user_id, car_id)

        return redirect('car_list')
    


        


