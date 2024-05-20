Instalare Git, Docker și Python

Instalare Git

       

sudo apt install git-all -y

Actualizare și Instalare Pachete Necesare

   

sudo apt-get update
sudo apt-get install ca-certificates curl gnupg lsb-release -y

Configurare Chei Docker

   

sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

Adăugare Repozitoriu Docker

   

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo chmod a+r /etc/apt/keyrings/docker.gpg
sudo apt-get update

Instalare Docker și Pluginuri

   

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-compose -y

Instalare Python și Pachete Adiționale

   

    sudo apt install python3-pip -y
    pip install flask
    pip install pytest
    sudo apt install gedit -y
    sudo apt install python3.10-venv -y

Clonare Repozitoriu de pe Git

    Acceptare invitație Git
        Verificați dacă ați acceptat invitația de pe Git trimisă de ivchrisp pentru curs_vcgj_442D_animale.
        Acceptați invitația prin Chrome logându-vă în contul vostru de Git de pe PC sau de pe VM.

    Clonare Repozitoriu

       

    git clone https://github.com/ivchrisp/curs_vcgj_442D_animale

        După rularea comenzii, ar trebui să aveți un director cu numele curs_vcgj_442D_animale.

    Navigare în Director
        În directorul clonat veți găsi fișierul 442D_animale.py și în subdirectorul lib fișierul biblioteca_animale.py.

Modificare Repozitoriu

    Verificare Stare Repozitoriu

       

git status

Creare și Comutare pe o Ramură Nouă

   

    git branch devel/NUMEGIT_ANIMALULVOSTRU
    git checkout devel/NUMEGIT_ANIMALULVOSTRU

Modificare Fisiere cu Animalul Vostru

    Modificare fișier 442D_animale.py
        Schimbați peste tot unde vedeți hamster cu animalul vostru.
        Inclusiv în denumirea funcțiilor. Puteți folosi un editor de text sau unelte de înlocuire automată precum replace all.

    Exemplu de fișier modificat (442D_animale.py):

    python

    from flask import Flask
    import lib.biblioteca_animale
    app = Flask(__name__)
    print('442D_animale')

    '''
     ------------------------------------
        NUMELE_TAU si GRUPA  - foca
     ------------------------------------
    '''

    @app.route("/foca", methods=['GET'])
    def obtine_foca():
        ret = "<h1>foca:</h1>"
        ret += "<b>Culoare: </b>"
        ret += lib.biblioteca_animale.culoare_foca()
        ret += "<br>"

        ret += "<b>Hrana: </b>"
        ret += lib.biblioteca_animale.hrana_foca()
        ret += "<br>"

        ret += "<b>Invelisul Corpului: </b>"
        ret += lib.biblioteca_animale.invelisul_corpului_foca()
        ret += "<br>"

        print("DBG: apel obtine_foca")
        return ret

    @app.route("/foca/culoare", methods=['GET'])
    def obtine_culoare_foca():
        ret = ""
        ret += lib.biblioteca_animale.culoare_foca()
        return ret

    @app.route("/foca/hrana", methods=['GET'])
    def obtine_hrana_foca():
        ret = ""
        ret += lib.biblioteca_animale.hrana_foca()
        return ret

    @app.route("/foca/invelisul_corpului", methods=['GET'])
    def obtine_invelisul_corpului_foca():
        ret = ""
        ret += lib.biblioteca_animale.invelisul_corpului_foca()
        return ret

    app.run(host="127.0.0.1", port=5002)

    Copiere fișier modificat în 442D_animale.py
        Utilizați un editor de text din Linux sau copiați fișierul direct prin navigarea în managerul de fișiere și dând click dreapta -> paste.

Concluzie

Prin urmarea acestor pași, veți avea un mediu configurat pentru dezvoltarea aplicației despre animalul vostru, în acest caz foca, utilizând Git, Docker și Python.
