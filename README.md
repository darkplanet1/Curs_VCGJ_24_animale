Am ales vulturul ca si animal
Pe masina virtuala de ubuntu am instalat git, docker, java, jenkins, python3, pytest

Pentru instalare docker am folosit instructiunile de pe site-ul oficial https://docs.docker.com/engine/install/ubuntu/
Iar pentru jenkins am folosit synaptic packet manager pentru a il instala

Comenzile utilizate au fost 
systemctl start jenkins
systemctl start docker
Pentru a porni jenkins si docker
Pentru a creea un container utilizam docker build -t NumeApp , iar pentru a rula docker run -p port_local:port_container NumeApp

Pentru git am utilizat comenzile
git config --global user.email stefan_c_tugui@yahoo.com
git config --global user.name "superdrago09"
git remote add origin git@github.com:darkplanet1/Curs_VCGJ_24_animale
git commit -m "Initial commit"
git checkout -b devel/Tugui_Stefan
git add .
git commit -m " "
git push origin
...
