from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello World")


def about(request):
    return HttpResponse("This is about page.")


def hello(request, first_name):
    return HttpResponse(f"Hello {first_name}")


def sum(request, first_number, second_number):
    result = first_number + second_number
    return HttpResponse(f"The total is: {result}")
