clear
e
exit
mkdir repos
sudo apt update
sudo apt full-upgrade
clear
sudo apt install python3-pip
git init
git add .
git commit -m "Initial commit of my project"
git config --global user.email "niharbastia297@gmail.com"
git config --global user.name "Nihar Bastia"
git commit -m "Initial commit of my project"
git remote add origin https://github.com/NB297/Weather-Data-Pipeline-Project
git push -u origin master
git reset HEAD^
git rm -r --cached .vscode-server/
git add .
git commit --amend --no-edit
git push -u origin master
pip show requests
ls
cd repos/weather-data-project/api-request
python3 api_request.py
git add .
git commit -m "Changes in api_request"
git push
cd repos/weather-data-project
docker-compose exec db psql -U db_user -d db
move repos/weather-data/project/api_request/docker-compose.yaml repos/weather-data
mv repos/weather-data/project/api_request/docker-compose.yaml repos/weather-data
mv repos/weather-data-project/api_request/docker-compose.yaml repos/weather-data-project
move repos/weather-data-project/api_request/docker-compose.yaml repos/weather-data-project
exit
mv repos/weather-data-project/api_request/docker-compose.yaml repos/weather-data-project
cd repos
mv repos/weather-data-project/api_request/docker-compose.yaml repos/weather-data-project
mv repos/weather-data-project/api-request/docker-compose.yaml repos/weather-data-project
exit
python3 api_request.py
cd repos/weather-data-project/api-request
python3 api_request.py
clear
python3 insert_records.py
clear
docker-compose up
mv repos/weather-data-project/api-request/docker-compose.yaml repos/weather-data-project
