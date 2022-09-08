#!/bin/bash
export mode=production
export DATABASE__NAME=testmgmt
export DATABASE__USER=testmgmtadmin
export DATABASE__PASSWORD=testmgmtadmin@123
export DATABASE__HOST=localhost
export DATABASE__PORT=5432

cd test_mgmt 
python3 manage.py runserver 0.0.0.0:8000
cd ..