from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Index(request):
    return HttpResponse("hello World!")

def Home(request):
    help_dict={"help_me":"I am here to help you"}
    return render(request, "first_app/help.html", context=help_dict)