from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
def TaskTwo(request):
    Dict={"inside_me":"Hello I am from AppTwo view,py file"}
    return render(request, "Second_App/index.html", context=Dict)

def TaskThree(request):
    return HttpResponse("Third Page")

def TaskFour(request,id):
    return HttpResponse(f"Here we can get ID, Name: {id}")

def Old_Url(request):
    return redirect("New_Url")

def New_Url_view(request):
    return HttpResponse("This is New Url")