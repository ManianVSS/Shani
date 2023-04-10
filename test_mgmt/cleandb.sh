#!/bin/bash


rm -rf api/migrations
rm -rf siteconfig/migrations
rm -rf requirements/migrations
rm -rf workitems/migrations
rm -rf testdesign/migrations
rm -rf automation/migrations
rm -rf execution/migrations
rm -rf people/migrations
rm data/db.sqlite3
bash migrate.sh
