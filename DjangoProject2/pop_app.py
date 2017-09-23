# -*- coding: utf-8 -*-

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject2.settings')


import django
django.setup()


## FAKE POP SCRIP
import random
from second_app.models import *
from faker import Faker


faker = Faker()


#TOPICS = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def populate(N=5):

    for entry in range(N):

        #top = add_topic()

        fake_name = faker.name()
        first = fake_name.split(' ')[0]
        last = fake_name.split(' ')[-1]

        fake_email = faker.email()
        fake_user = User.objects.get_or_create(
            full_name=fake_name,
            first_name=first,
            last_name=last,
            email=fake_email
        )[0]


if __name__ == '__main__':

    import sys

    print 'POPULATIN DATABASE'

    #print sys.argv

    #for arg in sys.argv:

        #print type(arg)

    x, y = [int(i) for i in sys.argv[1:]]

    populate(random.randint(x, y))

    #for i in range(random.randint(x, y)):

        #print i

    print 'POPULATED'