import librarie.biblioteca_urspanda as burspanda

def test_specie_urspanda():
    spec = burspanda.specie_urspanda()
    if spec == "urs" : 
        assert True
    else: 
        assert False
        

def test_zona_urspanda():
    zona = burspanda.zona_urspanda()
    if zona == "China" :
        assert True
    else: 
        assert False

def test_clasificare_urspanda():
    clasificare = burspanda.clasificare_urspanda()
    if clasificare == "carnivor" :
        assert True
    else: 
        assert False
        
        
def test_specie_pandarosu():
    spec = burspanda.specie_pandarosu()
    if spec == "pandarosu" : 
        assert True
    else: 
        assert False
        

def test_zona_pandarosu():
    zona = burspanda.zona_pandarosu()
    if zona == "India" :
        assert True
    else: 
        assert False

def test_clasificare_pandarosu():
    clas = burspanda.clasificare_pandarosu()
    if clas == "erbivor" :
        assert True
    else: 
        assert False  
