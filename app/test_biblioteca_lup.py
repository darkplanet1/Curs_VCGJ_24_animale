import librarie.biblioteca_lup as blup

def test_specie_lup():
    spec = blup.specie_lup()
    if spec == "lup" : 
        assert True
    else: 
        assert False
        

def test_zona_lup():
    zona = blup.zona_lup()
    if zona == "Europa" :
        assert True
    else: 
        assert False

def test_clasificare_lup():
    clasificare = blup.clasificare_lup()
    if clasificare == "periculos" :
        assert True
    else: 
        assert False
        
        
def test_specie_european():
    spec = blup.specie_european()
    if spec == "european" : 
        assert True
    else: 
        assert False
        

def test_zona_european():
    zona = blup.zona_european()
    if zona == "Europa" :
        assert True
    else: 
        assert False

def test_clasificare_european():
    clas = blup.clasificare_european()
    if clas == "periculos" :
        assert True
    else: 
        assert False  
