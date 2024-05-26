# Curs_VCGJ_24_animale
Proiect de Aplicație Web pentru Informații despre Animale

Descriere:

Proiectul urmărește dezvoltarea unei aplicații web care furnizează informații detaliate despre diverse animale. Utilizatorii vor putea afla detalii despre zonele și regiunile în care trăiesc aceste animale.

Tehnologii utilizate:

    Flask: Un framework web Python popular, care oferă o abordare simplă și rapidă pentru dezvoltarea aplicațiilor web.
    Git: Un sistem de control al versiunilor folosit pentru a gestiona colaborarea echipei și a urmări modificările codului.
    Docker: O platformă de containerizare ce permite rularea aplicației într-un mediu izolat și reproductibil.
    Jenkins: Un server de integrare continuă și livrare continuă (CI/CD) utilizat pentru automatizarea testelor și implementarea aplicației.

Structura proiectului:

    app: Directorul principal al aplicației web, care conține:
        442D_animale.py: Fișierul principal al aplicației, care definește rutele și funcțiile legate de animale.
        biblioteca_animale.py: Modul care conține funcții pentru extragerea informațiilor despre diverse animale.
        activeaza_venv: Script pentru activarea mediului virtual de lucru local.
        activeaza_venv_jenkins: Script pentru activarea mediului virtual de lucru în cadrul Jenkins.
        lib: Subdirector ce găzduiește module specifice pentru diferite funcționalități legate de animale.
            biblioteca_animale.py: Fișierul care definește informațiile despre animale.
    tests: Director ce conține fișierele de testare pentru funcționalitățile aplicației.
        test_biblioteca_animale.py: Fișierul de testare pentru funcțiile din modulul biblioteca_animale.
    Jenkinsfile: Fișierul de configurare pentru Jenkins Pipeline, care definește procesul de testare și implementare automată.

Beneficii:

    Acces facil la informații despre animale: Utilizatorii pot descoperi cu ușurință detalii despre o varietate de specii.
    Dezvoltare rapidă și ușoară: Flask simplifică crearea aplicației web.
    Colaborare eficientă: Git facilitează colaborarea echipei și urmărirea modificărilor codului.
    Implementare scalabilă: Docker permite rularea aplicației într-un mediu izolat și reproductibil, facilitând scalarea.
    Testare automată: Jenkins automatizează procesul de testare, asigurând calitatea aplicației.

