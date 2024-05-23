import librarie.biblioteca_tigru as btigru

def test_specie_tigru():
    spec = btigru.specie_tigru()
    if spec == "siberian" : 
        assert True
    else: 
        assert False
        

def test_zona_tigru():
    zona = btigru.zona_tigru()
    if zona == "Rusia" :
        assert True
    else: 
        assert False

def test_clasificare_tigru():
    clasificare = btigru.clasificare_tigru()
    if clasificare == "carnivor" :
        assert True
    else: 
        assert False
        
        
def test_specie_siberian():
    spec = btigru.specie_siberian()
    if spec == "siberian" : 
        assert True
    else: 
        assert False
        

def test_zona_siberian():
    zona = btigru.zona_siberian()
    if zona == "Rusia" :
        assert True
    else: 
        assert False

def test_clasificare_siberian():
    clas = btigru.clasificare_siberian()
    if clas == "carnivor" :
        assert True
    else: 
        assert False  
