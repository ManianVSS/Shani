from django.contrib.auth.models import User


def create_super_user():
    try:
        User.objects.get(username='admin2')
    except User.DoesNotExist:
        User.objects.create_superuser('admin2', 'admin@example.com', 'password')
