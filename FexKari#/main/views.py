from django.shortcuts import render

# Create your views here.
def vista1(request):
    return render(request, 'main/vista1.html')

def vista2(request):
    return render(request, 'main/vista2.html')

def vista3(request):
    return render(request, 'main/vista3.html')

def vista4(request):
    return render(request, 'main/vista4.html')

def vista5(request):
    return render(request, 'main/vista5.html')

def login(request):
    return render(request, 'main/login.html') 

