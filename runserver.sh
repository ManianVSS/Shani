#!/bin/bash
export mode=production
export DATABASE__NAME=testmgmt
export DATABASE__USER=testmgmtadmin
export DATABASE__PASSWORD=testmgmtadmin@123
export DATABASE__HOST=localhost
export DATABASE__PORT=5432

export DJANGO__SECRET_KEY='django-insecure-9=(@6%n=2c^$4%b1-0!7-k+=vjeo8pub3r&$$ijw(0tchsaxn4'
# export DEBUG=False
export DJANGO__bool__DEBUG=False

cd test_mgmt 
python3 manage.py runserver 0.0.0.0:8000 --insecure
cd ..