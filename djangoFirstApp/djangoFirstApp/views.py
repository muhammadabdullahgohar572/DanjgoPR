from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    # return HttpResponse("Hello, World!  This is a Home Page.")
    return render(request,'website/index.html')


def About(request):
    return HttpResponse("Hello, World!  This is a About Page.")




def Contact_us(request):
    return HttpResponse("Hello, World!  This is a Contact Page.")



