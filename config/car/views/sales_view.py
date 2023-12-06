from django.shortcuts import render
from django.views import View


class SalesList(View):
    def get(self, request):

        return render(request, 'sales.html', {

        })
    
    def post(self, request):
        return render(request, 'sales.html', {

        })

