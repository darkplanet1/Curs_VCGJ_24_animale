import librarie.biblioteca_elefant as belefant

def test_specie_elefant():
    spec = belefant.specie_elefant()
    if spec == "elefant" : 
        assert True
    else: 
        assert False
        

def test_zona_elefant():
    zona = belefant.zona_elefant()
    if zona == "Asia" :
        assert True
    else: 
        assert False

def test_clasificare_elefant():
    clasificare = belefant.clasificare_elefant()
    if clasificare == "nu de treaba" :
        assert True
    else: 
        assert False
        
        
def test_specie_african():
    spec = belefant.specie_african()
    if spec == "african" : 
        assert True
    else: 
        assert False
        

def test_zona_african():
    zona = belefant.zona_african()
    if zona == "Africa" :
        assert True
    else: 
        assert False

def test_clasificare_african():
    clas = belefant.clasificare_african()
    if clas == "de treaba" :
        assert True
    else: 
        assert False  
