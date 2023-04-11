# Shani

Test Management - Use-Cases, Requirements, BDD Test-Cases, TDD execution and dashboard

##### **Building dashboard **<br>
Pre-Requisites:</br>
Install latest nodejs using official documentation</br>
Note: Ubuntu package manager has older version of Node.. Please use latest from official website.</br>
> cd webui</br>
> yarn install</br>
> yarn build </br>
> cd ../test_mgmt/</br>
> ln -sf ../webui/build .</br>
> cd ..</br>

### **Development Setup**

##### **Installing python dependencies - Ubuntu**<br>
> sudo apt update</br>
> sudo apt install python3</br>
> sudo apt install pip</br>
> sudo apt install libpq-dev</br>
> cd test_mgmt</br>
> pip install -r requirements.txt</br>

##### **Creating and Migrating DB Schema**</br>
> cd test_mgmt</br>
> ./migrate.sh</br>

##### **Running server**
> cd test_mgmt</br>
> ./runserver.sh</br>

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

##### **Creating Postgres production DB and schema one time**</br>
> ./createdb.sh

##### **Migrating DB Schema for changes**</br>
> ./migrate.sh

##### **Running server**</br>
> ./runserver.sh

Admin console should be up on http://localhost:8000/admin
