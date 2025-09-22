from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from dashboard.models import Manager

class Command(BaseCommand):
    help = 'Reset manager password with proper hashing'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username of the manager')
        parser.add_argument('password', type=str, help='New password for the manager')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        
        try:
            manager = Manager.objects.get(username=username)
            manager.password = make_password(password)
            manager.save()
            self.stdout.write(
                self.style.SUCCESS(f'Successfully reset password for manager: {username}')
            )
        except Manager.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(f'Manager with username "{username}" does not exist')
            )
