import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'django_two.settings')

import django
django.setup()

from django_two_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for x in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

    # New Entry
        user = User.objects.get_or_create(first_name =fake_first_name,
                                      last_name = fake_last_name,
                                      email = fake_email)

if __name__ == '__main__':
    print('start')
    populate(20)
    print('Done')