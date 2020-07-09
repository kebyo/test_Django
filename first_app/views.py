from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def bigballs(request):
    return render(request, 'first_app/bigballs.html')