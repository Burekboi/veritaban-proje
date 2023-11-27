from django.shortcuts import render
from django.views import View


class ServiceCreate(View):
    def get(self, request):

        return render(request, 'car_service.html', {

        })
    
    def post(self, request):
        return render(request, 'car_list.html', {

        })

