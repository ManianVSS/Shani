#!/bin/bash
python3 manage.py shell -c "from create_sample_data import create; create()"