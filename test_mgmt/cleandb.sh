#!/bin/bash


rm -rf api/migrations
rm -rf automation/migrations
rm -rf siteconfig/migrations
rm data/db.sqlite3
bash migrate.sh
