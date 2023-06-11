from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, template_name='index.html')

def about(request):
    return HttpResponse("Welcome to About Page")

def contact(request):
    return HttpResponse("Welcome to contact Page")
