# -*- coding: utf-8 -*-

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject1.settings')


import django
django.setup()


## FAKE POP SCRIP
import random
from first_app.models import *
from faker import Faker


faker = Faker()


TOPICS = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():

    t = Topic.objects.get_or_create(name=random.choice(TOPICS))[0]
    t.save()

    return t


def populate(N=5):

    for entry in range(N):

        top = add_topic()

        fake_url = faker.url()
        fake_name = faker.company()
        webpage = WebPage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]

        fake_date = faker.date()

        record = AccessRecord.objects.get_or_create(webpage=webpage, date=fake_date)[0]


if __name__ == '__main__':

    import sys

    #print sys.argv

    #for arg in sys.argv:

        #print type(arg)

    x, y = [int(i) for i in sys.argv[1:]]

    populate(random.randint(x, y))

    #for i in range(random.randint(x, y)):

        #print i
