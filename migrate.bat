set mode=production
set DATABASE__NAME=testmgmt
set DATABASE__USER=testmgmtadmin
set DATABASE__PASSWORD=testmgmtadmin@123
set DATABASE__HOST=localhost
set DATABASE__PORT=5432

cd test_mgmt
python manage.py makemigrations api
python manage.py makemigrations siteconfig
python manage.py makemigrations requirements
python manage.py makemigrations workitems
python manage.py makemigrations testdesign
python manage.py makemigrations automation
python manage.py makemigrations execution
python manage.py makemigrations people
python manage.py migrate
python manage.py shell -c "from create_super_user import create_super_user; create_super_user()"
cd ..