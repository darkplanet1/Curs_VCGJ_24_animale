Proiectul constă în dezvoltarea unei aplicații web care să ofere informații despre diferite animale, precum culoarea, hrana preferată și învelișul corpului. Aplicația este construită folosind scriptul Flask în limbajul de programare Python.

Structura Proiectului

    app/ - Directorul principal al aplicației.
       442D_animale.py - Fișierul principal al aplicației care definește rutele și funcționalitățile asociate animalelor.
       biblioteca_animale.py - Modulul care conține funcții pentru a obține informații despre diferite animale.
       activeaza_venv - Script pentru activarea mediului virtual de lucru.
       activeaza_venv_jenkins - Script pentru activarea mediului virtual de lucru în Jenkins.
       lib/ - Directorul care conține modulele pentru funcționalitățile specifice animalelor.

    biblioteca_animale.py - Modulul care definește informațiile despre animale (culoare, hrana, învelișul corpului).

tests/ - Directorul care conține fișierele de testare pentru funcționalitățile aplicației.

    test_biblioteca_animale.py - Fișierul de testare pentru funcțiile din modulul biblioteca_animale.

Jenkinsfile - Fișierul de configurare pentru Jenkins Pipeline.

Arhitectură și Tehnologii

     Flask: Aplicația este construită utilizând scriptul Flask pentru Python, ceea ce oferă un mediu rapid și ușor de dezvoltare pentru crearea aplicațiilor web.

    Git: Proiectul este gestionat folosind Git, permițând colaborarea între membrii echipei și urmărirea modificărilor în cod.

    Docker: Docker este utilizat pentru gestionarea containerelor

    Jenkins: Jenkins este folosit pentru  testare  aplicației.
