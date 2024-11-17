#!/bin/bash
python3 manage.py shell -c "from test_mgmt.dataload import load_data_from_folder; load_data_from_folder(\"$1\")"