@echo off
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~2,2%" & set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%" & set "Min=%dt:~10,2%" & set "Sec=%dt:~12,2%"

set "datestamp=%YYYY%%MM%%DD%" & set "timestamp=%HH%%Min%%Sec%"
set "fullstamp=%YYYY%-%MM%-%DD%_%HH%-%Min%-%Sec%"
echo datestamp: "%datestamp%"
echo timestamp: "%timestamp%"
echo fullstamp: "%fullstamp%"

mkdir data\dbbackup\%fullstamp%\migrations

move api\migrations data\dbbackup\%fullstamp%\migrations\api
move siteconfig\migrations data\dbbackup\%fullstamp%\migrations\siteconfig
move requirements\migrations data\dbbackup\%fullstamp%\migrations\requirements
move workitems\migrations data\dbbackup\%fullstamp%\migrations\workitems
move scheduler\migrations data\dbbackup\%fullstamp%\migrations\scheduler
move testdesign\migrations data\dbbackup\%fullstamp%\migrations\testdesign
move automation\migrations data\dbbackup\%fullstamp%\migrations\automation
move execution\migrations data\dbbackup\%fullstamp%\migrations\execution
move people\migrations data\dbbackup\%fullstamp%\migrations\people
move program\migrations data\dbbackup\%fullstamp%\migrations\program
