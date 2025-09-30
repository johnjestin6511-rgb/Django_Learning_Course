from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
# Create your views here.

posts=[
    {'id':1,'title': 'Post 1', 'content': 'Content for post 1'},
    {'id':2,'title': 'Post 2', 'content': 'Content for post 2'},
    {'id':3,'title': 'Post 3', 'content': 'Content for post 3'},
    {'id':4,'title': 'Post 4', 'content': 'Content for post 4'}
]
def index(request):
    App_Title = "Latest App"
    return render(request, 'First_App/index.html', {"App_Title":App_Title, 'posts': posts})

def details(request,id):
    post=next((item for item in posts if item['id']== int(id)), None)
    #----------debugging with logging module-----------
    # logger=logging.getLogger("TESTING")
    # logger.debug(f"Post with ID {post} not found")
    return render(request, 'First_App/details.html', {'post':post})

def old_url_redirect(request):
    return redirect(reverse('First:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the new URL.")

def Html_page(request):
    my_dict ={ 'insert_me': " Hello I am from views.py file"}
    return render(request, 'html/index.html', context=my_dict)

