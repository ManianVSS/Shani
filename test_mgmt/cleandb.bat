@echo off
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~2,2%" & set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%" & set "Min=%dt:~10,2%" & set "Sec=%dt:~12,2%"

set "datestamp=%YYYY%%MM%%DD%" & set "timestamp=%HH%%Min%%Sec%"
set "fullstamp=%YYYY%-%MM%-%DD%_%HH%-%Min%-%Sec%"
echo datestamp: "%datestamp%"
echo timestamp: "%timestamp%"
echo fullstamp: "%fullstamp%"

mkdir data\dbbackup\%fullstamp%

move api\migrations data\dbbackup\%fullstamp%
move siteconfig\migrations data\dbbackup\%fullstamp%
move requirements\migrations data\dbbackup\%fullstamp%
move workitems\migrations data\dbbackup\%fullstamp%
move scheduler\migrations data\dbbackup\%fullstamp%
move testdesign\migrations data\dbbackup\%fullstamp%
move automation\migrations data\dbbackup\%fullstamp%
move execution\migrations data\dbbackup\%fullstamp%
move people\migrations data\dbbackup\%fullstamp%
move program\migrations data\dbbackup\%fullstamp%

move data\db.sqlite3 data\dbbackup\%fullstamp%

call migrate.bat
python manage.py shell -c "from create_super_user import create_super_user; create_super_user()"
python manage.py shell -c "from api.models import create_default_configuration; create_default_configuration()"