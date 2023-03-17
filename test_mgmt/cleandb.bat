del /s /q api\migrations
del /s /q automation\migrations
del /s /q siteconfig/migrations
del /s /q data\db.sqlite3
migrate.bat
python manage.py createsuperuser
