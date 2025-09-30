from django.shortcuts import render
from first_app.models import AccessRecord, Topic, Webpage, User

# Create your views here.
def index(request):
    web_list=AccessRecord.objects.order_by('date')
    date_dict ={'access_record':web_list}
    return render(request, 'first_app/index.html',context=date_dict )

def user(request):
    user_list = User.objects.all()
    user_dict = {"user_record" : user_list}
    return render(request, 'first_app/userpage.html', context= user_dict)
