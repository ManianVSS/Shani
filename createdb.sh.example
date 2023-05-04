#!/bin/bash
sudo -u postgres psql -c "create database testmgmt"
sudo -u postgres psql -c "create user testmgmtadmin with encrypted password 'testmgmtadmin@123'"
sudo -u postgres psql -c "grant all privileges on database testmgmt to testmgmtadmin"

./migrate.sh
