from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.db import connection
import os
from datetime import datetime
import pandas as pd
import pyodbc
import openpyxl




class ServiceCreate(View):
    
    def get(self, request, pk):
        os.system("cls")
        print("pk:", self.kwargs.get('pk'))
        with connection.cursor() as cursor:
            cursor.execute(
                f"EXEC get_sold_cars @user_id={self.kwargs.get('pk')}"
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
            "solded_cars": solded_cars,
            "pk": self.kwargs.get('pk')
        })

    def post(self, request, pk):
        os.system("cls")
        print("pk:", self.kwargs.get('pk'))
        service_car_id = request.POST.get('service_model')
        service_type = request.POST.get('service_type')
        service_date = request.POST.get('service_date')
        service_notes = request.POST.get('service_notes') 
        
        print(service_car_id, service_type, service_date, service_notes)
        with connection.cursor() as cursor:
            cursor.execute("exec dbo.add_service @arac_id=%s, @type=%s, @date=%s,  @notes=%s",
                [int(service_car_id), service_type, service_date, service_notes]
            )
            cursor.commit()
        return redirect("car_list")
    

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
    

class ServiceExcelConvert(View):
    def get(self, request):
        os.system("cls")
        conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=arabasatis;Trusted_Connection=yes;'

        # SQL verilerini bir DataFrame'e yükle
        conn = pyodbc.connect(conn_str)
        # cursor = conn.cursor()

        # Stored procedure'ı çağırma
        # cursor.execute("exec dbo.get_services")
        sql_query = "exec dbo.get_services"

        # Sonuçları al
        # result = cursor.fetchall()

        # Verileri al
        data = pd.read_sql(sql_query, conn)

        # Excel dosyasına yazma
        excel_filename = 'output.xlsx'  # Kaydedilecek Excel dosyasının adı
        data.to_excel(excel_filename, index=False)

        # Bağlantıyı kapat
        conn.close()

        return render(request, 'service_table.html', {
            "text": f'Excel dosyası {excel_filename} olarak kaydedildi.'
        })
    

class ServiceExcelImport(View):
     def post(self,reqeust):
        os.system("cls")
        excel_file = self.request.FILES.get('excel_file')
        print(excel_file)
        if excel_file:
            # try:
                # Veritabanına bağlantı kurma
                connection = pyodbc.connect(
                    'DRIVER={ODBC Driver 17 for SQL Server};'
                    'SERVER=localhost;'
                    'DATABASE=arabasatis;'
                    'Trusted_Connection=yes;'
                )
                cursor = connection.cursor()

                # Excel dosyasını okuma
                df = pd.read_excel(excel_file)

                # Veritabanına kaydetme işlemleri
                for index, row in df.iterrows():
                    print(row)
                    cursor.execute("exec dbo.import_excel @user=?, @car_model=?, @types=?, @notes=?", 
                                   row["user"], row['car_model'], row['types'], row['notes']
                                   )

                # Değişiklikleri kaydet ve bağlantıyı kapat
                connection.commit()
                connection.close()

                return redirect('service_list')  # Başarıyla yüklendiyse başka bir sayfaya yönlendir
            # except Exception as e:
            #     return HttpResponse(f'Hata oluştu: {e}')        
