import librarie.biblioteca_Pisica as bPisica

def test_specie_Pisica():
    spec = bPisica.specie_Pisica()
    if spec == "European" : 
        assert True
    else: 
        assert False
        

def test_zona_Pisica():
    zona = bPisica.zona_Pisica()
    if zona == "Romania" :
        assert True
    else: 
        assert False

def test_clasificare_Pisica():
    clasificare = bPisica.clasificare_Pisica()
    if clasificare == "carnivor" :
        assert True
    else: 
        assert False
        
        
def test_specie_European():
    spec = bPisica.specie_European()
    if spec == "European" : 
        assert True
    else: 
        assert False
        

def test_zona_European():
    zona = bPisica.zona_European()
    if zona == "Romania" :
        assert True
    else: 
        assert False

def test_clasificare_European():
    clas = bPisica.clasificare_European()
    if clas == "carnivor" :
        assert True
    else: 
        assert False  
