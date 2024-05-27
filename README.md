Am ales Rinocerul ca si animal

Pe mac OS cu ajutorul homebrew am instalat din terminal Git, Docker, Jenkins

Pentru instalare docker am folosit instructiunile de pe site-ul oficial https://docs.docker.com/engine/install/ubuntu/

Comenzile utilizate au fost
brew services start jenkins-lts
docker pull python:3.8-alpine
docker login
Pentru a porni jenkins si docker

Pentru a creea un container utilizam docker build -t your-app-name , iar pentru a rula docker run -p port_local:port_container NumeApp

Pentru git am utilizat comenzile
git config --global user.email andreidragu27@yahoo.com
git config --global user.name "andreidraguu"
git remote add origin git@github.com:darkplanet1/Curs_VCGJ_24_animale
git commit -m "Initial commit"
git checkout -b devel/andreidraguu
git add *
git commit -m ""  
git push --set-upstream origin devel/ andreidraguu
...
