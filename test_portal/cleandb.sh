#!/bin/bash

timestamp=$(date +%F-%H:%M)
mkdir -p data/dbbackup/$timestamp/migrations

mv api/migrations data/dbbackup/$timestamp/migrations/api
mv siteconfig/migrations data/dbbackup/$timestamp/migrations/siteconfig
mv requirements/migrations data/dbbackup/$timestamp/migrations/requirements
mv workitems/migrations data/dbbackup/$timestamp/migrations/workitems
mv scheduler/migrations data/dbbackup/$timestamp/migrations/scheduler
mv testdesign/migrations data/dbbackup/$timestamp/migrations/testdesign
mv automation/migrations data/dbbackup/$timestamp/migrations/automation
mv execution/migrations data/dbbackup/$timestamp/migrations/execution
mv people/migrations data/dbbackup/$timestamp/migrations/people
mv program/migrations data/dbbackup/$timestamp/migrations/program

mv data/db.sqlite3 data/dbbackup/$timestamp

bash migrate.sh
python manage.py create_super_user
python manage.py create_default_configuration