Proiect site animale => Urs Panda

Am instalat pe masina virtuala python3, pytest, jenkins, docker, git, java

sudo apt update

sudo apt install python3

sudo apt install git

sudo apt install python3-pip

pip3 install pytest

Pentru instalare docker: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04

Pentru instalare jenkins: https://www.cherryservers.com/blog/how-to-install-jenkins-on-ubuntu-22-04

![1st screenshot](https://github.com/crchende/jenkinsdemo/assets/161889050/62da0cf3-00ea-4c61-962d-4b5ed7253f54)


Fisierele din proiect: 

![2nd photo](https://github.com/crchende/jenkinsdemo/assets/161889050/c4f550c2-c33d-47e8-b603-a01dc7ba7b7e)


Fisier Dockerfile:

![Poza11](https://github.com/crchende/jenkinsdemo/assets/161889050/41cf1f17-fcd6-4352-b35d-d7e0ba7b48d2)

Fisier Jenkinsfile: 

![Poza 12 1](https://github.com/crchende/jenkinsdemo/assets/161889050/b84d545e-3247-48dc-b1d3-5ac140cba038)
![Poza 12 2](https://github.com/crchende/jenkinsdemo/assets/161889050/8a37d35f-8d67-45b2-90a7-d0912f5983f7)

Fisierele din app: 

![poza 3](https://github.com/crchende/jenkinsdemo/assets/161889050/674f4a26-f92e-43b9-887c-d531a2ce0b0c)


Folder librarie: 

![4 1poza](https://github.com/crchende/jenkinsdemo/assets/161889050/3d217f1f-768f-416f-b1a8-12916a2df5fb)
![4 2poza](https://github.com/crchende/jenkinsdemo/assets/161889050/fc8be62e-b90f-44db-b03b-221d3c623993)

Fisier test_biblioteca_urspanda: 

![5poza](https://github.com/crchende/jenkinsdemo/assets/161889050/aa50527e-a989-4b8a-842a-29c63782ddfb)


Fisier aplicatie 442D_urspanda: 
![poza6](https://github.com/crchende/jenkinsdemo/assets/161889050/c135d52b-7362-4c9e-8cf7-5c9f8a9f1447)
![poza6 1](https://github.com/crchende/jenkinsdemo/assets/161889050/b3a3f161-43dd-4e0f-8d68-b61ba168c1a3)

Fisier Dockerfile: 

![Poza7](https://github.com/crchende/jenkinsdemo/assets/161889050/2ef973ae-285b-4663-a490-e74e59f3584e)

Fisier activeaza_venv

![Poza8](https://github.com/crchende/jenkinsdemo/assets/161889050/6ba4eea1-3c46-4f49-be92-61649bb069f1)

Fisier activeaza_venv_jenkins:

![Poza9](https://github.com/crchende/jenkinsdemo/assets/161889050/8550f204-81cb-4f25-a837-0c93a8fbacae)

Fisier requirements:

![Poza10](https://github.com/crchende/jenkinsdemo/assets/161889050/6a50963e-7b43-4f23-9779-602dde8717cf)


Comenzi necesare pentru docker"

docker build -t NumeApp .
docker run -p port_local:port_container NumeApp
Daca totul functioneaza corect trebuie sa primim un mesaj asemanator :

![nou1](https://github.com/crchende/jenkinsdemo/assets/161889050/a6057962-9f47-4038-8a15-132f4c181df7)

![nou2](https://github.com/crchende/jenkinsdemo/assets/161889050/7a0905d2-3a27-4103-8083-9762b33922af)

Rulare teste pytest:

![nou3](https://github.com/crchende/jenkinsdemo/assets/161889050/12630a68-6c43-4d98-8a8e-f8edaeca2fae)

Aplicatie:

![nou4](https://github.com/crchende/jenkinsdemo/assets/161889050/464671ef-7bb2-4020-8173-734611b16f85)
![nou6](https://github.com/crchende/jenkinsdemo/assets/161889050/83d5d11c-f562-4cff-859e-d9a08da43f07)

Testare jenkins:

![pozenou](https://github.com/crchende/jenkinsdemo/assets/161889050/5a242c59-415d-4daf-9b76-d2581e5c4b70)

