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
