#!/bin/bash

bash cleanmigrations.sh
rm data/db.sqlite3

bash migrate.sh
python manage.py shell -c "from create_super_user import create_super_user; create_super_user()"