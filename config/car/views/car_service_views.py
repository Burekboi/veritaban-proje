from django.shortcuts import render
from django.views import View
from django.db import connection


class ServiceCreate(View):
    def get(self, request):

        return render(request, 'car_service.html', {

        })
    
    def post(self, request):
        return render(request, 'car_list.html', {

        })
    

class ServiceList(View):
    def get(self, request):
        servisler = [
            {
                'id': 1,
                'arabaMarka': 'Toyota',
                'arabaModel': 'Corolla',
                'servisTuru': 'Bakım',
                'servisTarihi': '2023-01-15',
                'ekNotlar': 'Yağ değişimi yapıldı.'
            },
            {
                'id': 2,
                'arabaMarka': 'Ford',
                'arabaModel': 'Focus',
                'servisTuru': 'Tamir',
                'servisTarihi': '2023-02-20',
                'ekNotlar': 'Ön fren değişimi yapıldı.'
            },
            {
                'id': 3,
                'arabaMarka': 'Honda',
                'arabaModel': 'Civic',
                'servisTuru': 'Lastik Değişimi',
                'servisTarihi': '2023-03-10',
                'ekNotlar': '4 lastik değişimi tamamlandı.'
            }
        ]
        return render(request, 'service_table.html', {
            "servisler": servisler
        })
    
    def post(self, request):
        return render(request, 'service_table.html', {

        })

