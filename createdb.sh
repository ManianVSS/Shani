#!/bin/bash
apt install postgresql
systemctl start postgresql.service
sudo -u postgres psql -c "create database testmgmt"
sudo -u postgres psql -c "create user testmgmtadmin with encrypted password 'testmgmtadmin@123'"
sudo -u postgres psql -c "grant all privileges on database testmgmt to testmgmtadmin"

export mode=production
export DATABASE__NAME=testmgmt
export DATABASE__USER=testmgmtadmin
export DATABASE__PASSWORD=testmgmtadmin@123
export DATABASE__HOST=localhost
export DATABASE__PORT=5432

cd test_mgmt && python3 manage.py makemigrations api && python3 manage.py migrate && cd ..
cd test_mgmt && echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'password')" | python manage.py shell && cd ..