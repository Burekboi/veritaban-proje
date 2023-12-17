from django.shortcuts import render, redirect
from django.views import View
from django.db import connection


class SalesList(View):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC get_sales"
                )
            result = cursor.fetchone()
            sales = []
            if result:
                columns = [col[0] for col in cursor.description]
                sales_dict = {columns[i]: result[i] for i in range(min(len(columns), len(result)))}
                sales.append(sales_dict)
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
                "EXEC add_sales @name=%s, @email=%s, @creditCard=%s",
                [name, email , creditCard]
                )
            cursor.commit()

        return redirect('car_list')

