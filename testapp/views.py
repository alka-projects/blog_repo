from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'testapp/home.html')
def one(request):
    return render(request,'testapp/1.html')
def edit1(request):
    return render(request,'testapp/edit1.html')
