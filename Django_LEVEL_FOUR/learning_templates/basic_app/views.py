from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {"name":"hello World!", "number":100}
    return render(request,'basic_app/index.html',context=context_dict)

def other(request):
    return render(request,'basic_app/other.html')

def relative_url_template(request):
    return render(request,'basic_app/relative_url_template.html')
# def index(request):
#     return render(request,'basic_app/index.html')