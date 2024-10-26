#!/bin/bash

timestamp=$(date +%F-%H:%M)
mkdir -p data/dbbackup/$timestamp/migrations

mv api/migrations data/dbbackup/$timestamp/migrations/api
mv siteconfig/migrations data/dbbackup/$timestamp/migrations/siteconfig
mv requirements/migrations data/dbbackup/$timestamp/migrations/requirements
mv workitems/migrations data/dbbackup/$timestamp/migrations/workitems
mv testdesign/migrations data/dbbackup/$timestamp/migrations/testdesign
mv automation/migrations data/dbbackup/$timestamp/migrations/automation
mv execution/migrations data/dbbackup/$timestamp/migrations/execution
mv people/migrations data/dbbackup/$timestamp/migrations/people
mv program/migrations data/dbbackup/$timestamp/migrations/program

mv data/db.sqlite3 data/dbbackup/$timestamp
mv data/replica.sqlite3 data/dbbackup/$timestamp

bash migrate.sh
python manage.py shell -c "from create_super_user import create_super_user; create_super_user()"
python manage.py shell -c "from api.models import create_default_configuration; create_default_configuration()"