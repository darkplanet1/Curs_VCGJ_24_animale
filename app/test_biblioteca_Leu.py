import librarie.biblioteca_Leu as bLeu

def test_specie_Leu():
    spec = bLeu.specie_Leu()
    if spec == "American" : 
        assert True
    else: 
        assert False
        

def test_zona_Leu():
    zona = bLeu.zona_Leu()
    if zona == "Chile" :
        assert True
    else: 
        assert False

def test_clasificare_Leu():
    clasificare = bLeu.clasificare_Leu()
    if clasificare == "carnivor" :
        assert True
    else: 
        assert False
        
        
def test_specie_American():
    spec = bLeu.specie_American()
    if spec == "American" : 
        assert True
    else: 
        assert False
        

def test_zona_American():
    zona = bLeu.zona_American()
    if zona == "Chile" :
        assert True
    else: 
        assert False

def test_clasificare_American():
    clas = bLeu.clasificare_American()
    if clas == "carnivor" :
        assert True
    else: 
        assert False  
