from django.core.management.base import BaseCommand

from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create Superuser and some test users'

    def add_arguments(self, parser):
        parser.add_argument('count, type=int')

    def handle(self, *args, **options):
        User.objects.all().delete()
        user_count = options['count']
        User.objects.create_superuser('Nikola', 'Nikola@drf.ru', 'drf1')
        for i in range(user_count):
            User.objects.create_user(f'user{i}', f'user{i}@drftest.ru', 'drf1')

        print('done')
