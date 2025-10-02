from django.shortcuts import render
from . import forms

# Create your views here.

def index(request):
    return render(request,'first_app/index.html')

def form_name_view(request):
    form = forms.Formname()

    if request.method=="POST":
        form = forms.Formname(request.POST)

        if form.is_valid():
            print("Validation Succes!")
            print(f"Name: {form.cleaned_data['Name']}")
            print(f"Email: {form.cleaned_data['Email']}")
            print(f"Text: {form.cleaned_data['Text']}")

    return render(request,'first_app/form_page.html',{'Form':form})
