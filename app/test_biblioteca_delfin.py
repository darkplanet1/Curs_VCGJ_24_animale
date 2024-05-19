import librarie.biblioteca_delfin as bdelfin

def test_specie_delfin():
    spec = bdelfin.specie_delfin()
    if spec == "delfin" : 
        assert True
    else: 
        assert False
        

def test_zona_delfin():
    zona = bdelfin.zona_delfin()
    if zona == "Yangtze" :
        assert True
    else: 
        assert False

def test_clasificare_delfin():
    clasificare = bdelfin.clasificare_delfin()
    if clasificare == "foarte inteligent" :
        assert True
    else: 
        assert False
        
        
def test_specie_delfin():
    spec = bdelfin.specie_delfin()
    if spec == "delfin" : 
        assert True
    else: 
        assert False
        

def test_zona_Baiji():
    zona = bdelfin.zona_Baiji()
    if zona == "Yangtze" :
        assert True
    else: 
        assert False

def test_clasificare_Baiji():
    clas = bdelfin.clasificare_Baiji()
    if clas == "inteligent" :
        assert True
    else: 
        assert False  
