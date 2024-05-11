#!/bin/bash
python3 manage.py shell -c "from create_super_user import create_super_user; create_super_user()"
python3 manage.py shell -c "from api.models import create_default_configuration; create_default_configuration()"