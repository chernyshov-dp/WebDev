import os
import django
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProTwo.settings")
django.setup()
from AppTwo.models import User

fakegen = Faker()


def populate(n=10):
    for entry in range(n):
        full_name = fakegen.name()
        fake_first_name = full_name.split(' ')[0]
        fake_last_name = full_name.split(' ')[1]
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]


if __name__ == '__main__':
    print("Populating script!")
    populate(50)
    print("Populating complete!")
