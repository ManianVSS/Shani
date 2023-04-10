# Shani

Test Management - Use-Cases, Requirements, BDD Test-Cases, TDD execution and dashboard

### **Development Setup**

Note: Dashboard development setup is yet to be documented

##### **Installing python dependencies - Ubuntu**<br>

> sudo apt update</br>
> sudo apt install python3</br>
> sudo apt install pip</br>
> sudo apt install libpq-dev</br>
> cd test_mgmt</br>
> pip install -r requirements.txt</br>

##### **Creating and Migrating DB Schema**</br>

> cd test_mgmt && python3 manage.py makemigrations api && python3 manage.py migrate && python manage.py createsuperuser
> && cd ..</br>

##### **Running server**

> cd test_mgmt</br>
> python manage.py runserver 0.0.0.0:8000</br>

Admin console should be up on http://localhost:8000/admin

### **Production Setup**

##### **Installing python dependencies - Ubuntu**<br>

> sudo apt update</br>
> sudo apt install python3</br>
> sudo apt install pip</br>
> sudo apt install postgresql</br>
> sudo systemctl enable postgresql.service </br>
> sudo systemctl start postgresql.service </br>
> sudo apt install libpq-dev</br>
> cd test_mgmt</br>
> pip install -r requirements.txt</br>

##### **Creating Postgres production DB**</br>

> sudo -u postgres psql -c "create database testmgmt"</br>
> sudo -u postgres psql -c "create user testmgmtadmin with encrypted password 'testmgmtadmin@123'"</br>
> sudo -u postgres psql -c "grant all privileges on database testmgmt to testmgmtadmin"</br>

##### **Creating and Migrating DB Schema**</br>

> sudo bash createdb.sh</br></br>
> **or**</br></br>
> export mode=production</br>
> export DATABASE__NAME=testmgmt</br>
> export DATABASE__USER=testmgmtadmin</br>
> export DATABASE__PASSWORD=testmgmtadmin@123</br>
> export DATABASE__HOST=localhost</br>
> export DATABASE__PORT=5432</br>
> cd test_mgmt && python3 manage.py makemigrations api && python3 manage.py migrate && python manage.py createsuperuser
> && cd ..</br>

##### **Running server**

> cd test_mgmt</br>
> export DJANGO__SECRET_KEY='django-insecure-9=(@6%n=2c^$4%b1-0!7-k+=vjeo8pub3r&$$ijw(0tchsaxn4'</br>
> export DJANGO__bool__DEBUG=False</br>
> python manage.py runserver 0.0.0.0:8000 --insecure</br>

Admin console should be up on http://localhost:8000/admin
