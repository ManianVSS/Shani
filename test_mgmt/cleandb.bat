cleanmigrations.bat
del /s /q data\db.sqlite3

migrate.bat
python manage.py shell -c "from create_super_user import create_super_user; create_super_user()"
python manage.py shell -c "from api.models import create_default_configuration; create_default_configuration()"