#хранит функции-представления,  которые говорят, что должно произойти по конкретному пути
from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request,'about.html')

def reverse(request):
    user_text = request.GET['username']
    reversed_text = user_text[::-1]
    return render(request,'reverse.html', {'word':reversed_text})

def home(request):
    # return HttpResponse('This is my home')
    return render(request, 'home.html')