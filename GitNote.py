#Test version Git
git version
#Name git
git config --global user.name "cuacaptaolau"
#Name email
git config --global user.email 'whydoyou217@gmail.com'
#Test config git
git config --list
#Create local repo
#cd folder
git init
# connect github
git remote add origin <url_github>
#<url_github> : code/clone/https
https://github.com/cuacaptaolau/Github_CodePython.git
#Down remote Repo on Github to local PC

#add file to git
git add <tenfile>
#add all changes
git add .
#Save Snapshots file
git commit -m "messages"
#changes comit
git commit --amend -m "messages changes"
#uploads all local to github
git push origin <folder> # folder = 'master' if root folder
#Views status git
git status