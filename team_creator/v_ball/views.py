from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse


#def index(request):
    #return HttpResponse("let's play Volleyball!")

def base(request):
    return render(request, 'base.html',{})

def home(request):
    return render(request, 'home.html', {})