#!/bin/bash
python3 manage.py shell -c "from test_mgmt.dataload import save_data_to_folder; save_data_to_folder(\"$1\")"