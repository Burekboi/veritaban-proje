from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        real_username = "admin"
        real_password = "admin"

        if real_username == username and real_password == password:
            print("Giriş başarılı")
            return redirect('car_list')  # Giriş başarılıysa yönlendirilecek sayfa
        else:
            return HttpResponse("Invalid login credentials")  # Giriş başarısızsa hata mesajı

    return render(request, 'login.html')
