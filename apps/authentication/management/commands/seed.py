from threading import local
from django_seed import Seed
from apps.authentication.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        help = "seed database for testing and development."
        seeder = Seed.seeder(locale='fr_FR')
        
        from apps.consulting.models import Practice, Service

        seeder.add_entity(User, 5, {
            'username': lambda x:seeder.faker.user_name(),
            'password': lambda x: seeder.faker.password(),
            'postal':  lambda x: seeder.faker.postcode(),
            'address':  lambda x: seeder.faker.address(),
            'country':  lambda x: seeder.faker.current_country(),
            'city':  lambda x: seeder.faker.city(),
        })
        seeder.add_entity(Practice, 5, {
            'website': lambda x:seeder.faker.domain_name(),
            'zipcode':  lambda x: seeder.faker.postcode(),
            'address':  lambda x: seeder.faker.address(),
            'city':  lambda x: seeder.faker.city(),
            'phone': lambda x: seeder.faker.phone_number()
        })
        seeder.add_entity(Service, 5, {
            'price': lambda x:seeder.faker.port_number(),
        })
        seeder.execute()
        
    