from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from .models import School,Student
from django.urls import reverse_lazy
# Create your views here.
# def index(request):
#     return render(request, "index.html")

# class CBview(View):
#     def get(self,request):
#         return HttpResponse("Welcome this is Class of CBview function")

class CBTemplateView(TemplateView):
    template_name = "index.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["Injectme"] = "This from TemplateView Class"
#         return context

class SchoolListView(ListView):
    context_object_name = 'schools_list'
    model = School
    template_name ='basic_app/school_ListView.html'

class StudentDetailsView(DetailView):
    context_object_name =  'school_detail'
    model = School
    template_name = 'basic_app/school_details.html'

class SchoolCreateView(CreateView):
    fields = '__all__'
    model = School

class SchoolUpdateView(UpdateView):
    fields = '__all__'
    model = School

class SchoolDeleteView(DeleteView):
    model = School
    template_name = 'basic_app/school_confrim_delete.html'
    success_url = reverse_lazy('basic_app:list')