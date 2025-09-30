import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstproject.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord, Topic , Webpage,User
from faker import Faker


fakegen = Faker()
topics=["Search", 'Social', 'MarketPlace','News','Games']

def add_topics():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

        top = add_topics()

        fake_Url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webp = Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_Url)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webp,date=fake_date)[0]

def add_user(N=5):
    for entry in range(N):
        fake_Fname = fakegen.first_name()
        fake_Lname = fakegen.last_name()
        fake_email = fakegen.email()

        fakeUser=User.objects.get_or_create(First_Name=fake_Fname,Last_Name=fake_Lname,Email=fake_email)[0]


if __name__== '__main__':
    # print("populating Script!")
    # populate(20)
    # print("Populating Completed!")

    print("populating Script!")
    add_user(20)
    print("Populating Completed!")


