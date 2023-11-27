from django.shortcuts import render
from django.views import View


class CarList(View):
    def get(self, request):
        araclar = [
    {
        'id': 1,
        'marka': 'Ford',
        'model': 'Mustang GT Fastback',
        'yil': 2022,
        'durum': 'Sıfır',
        'resim': 'https://www.log.com.tr/wp-content/uploads/2022/03/hayalleri-susleyecek-tamamen-elektrikli-ford-mustang-fastback-9.jpg',
        'motor_hacmi': '5.0 L',
        'yakit_turu': 'Benzin',
        'sanziman_tipi': 'Manuel',
        'cekis_sistemi': 'Arka Tekerlekten Çekiş',
        'beygir': 450,
        'fiyat': 750000  # Örnek bir fiyat, gerçek fiyatı kendi ihtiyaçlarınıza göre ayarlayabilirsiniz
    },

    {
        'id': 2,
        'marka': 'Tesla',
        'model': 'Model 3',
        'yil': 2023,
        'durum': 'Sıfır',
        'resim': 'https://www.tesla.com/sites/default/files/model3-new/social/model-3-hero-social.jpg',
        'motor_hacmi': 'Elektrikli',
        'yakit_turu': 'Elektrik',
        'sanziman_tipi': 'Otomatik',
        'cekis_sistemi': 'Dört Tekerlekten Çekiş',
        'beygir': 450,
        'fiyat': 1200000  # Örnek bir fiyat, gerçek fiyatı kendi ihtiyaçlarınıza göre ayarlayabilirsiniz
    },
    {
        'id': 3,
        'marka': 'Renault',
        'model': 'Symbol',
        'yil': 2014,
        'durum': 'İkinci El',
        'resim': 'https://i0.shbdn.com/photos/30/12/97/x5_11293012975iw.jpg',
        'motor_hacmi': '1.5 L',
        'yakit_turu': 'Dizel',
        'sanziman_tipi': 'Manuel',
        'cekis_sistemi': 'Ön Tekerlekten Çekiş',
        'beygir': 90,
        'fiyat': 80000  # Örnek bir fiyat, gerçek fiyatı kendi ihtiyaçlarınıza göre ayarlayabilirsiniz
    }
]



        return render(request, 'car_list.html', {
            'araclar': araclar
        })
    
    def post(self, request):
        return render(request, 'car_list.html', {

        })


class CarDetail(View):
    def get(self, request, pk):
        return render(request, 'car_detail.html', {

        })
    
    def post(self, request):
        return render(request, 'car_detail.html', {
            
        })
    

class CarCreate(View):
    def get(self, request):
        return render(request, 'car_create.html', {

        })
    
    def post(self, request):
        return render(request, 'car_create.html', {

        })


class CarUpdate(View):
    def get(self, request, pk):
        return render(request, 'car_update.html', {

        })
    
    def post(self, request):
        return render(request, 'car_update.html', {

        })
    

class CarDelete(View):
    def get(self, request, pk):
        return render(request, 'car_delete.html', {

        })
    
    def post(self, request):
        return render(request, 'car_delete.html', {

        })