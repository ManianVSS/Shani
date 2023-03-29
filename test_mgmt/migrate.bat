python manage.py makemigrations api
python manage.py makemigrations automation
python manage.py makemigrations siteconfig
python manage.py migrate

python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'password')"
