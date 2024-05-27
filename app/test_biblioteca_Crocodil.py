import librarie.biblioteca_Crocodil as bCrocodil

def test_specie_Crocodil():
    spec = bCrocodil.specie_Crocodil()
    if spec == "African" : 
        assert True
    else: 
        assert False
        

def test_zona_Crocodil():
    zona = bCrocodil.zona_Crocodil()
    if zona == "Madagascar" :
        assert True
    else: 
        assert False

def test_clasificare_Crocodil():
    clasificare = bCrocodil.clasificare_Crocodil()
    if clasificare == "carnivor" :
        assert True
    else: 
        assert False
        
        
def test_specie_African():
    spec = bCrocodil.specie_African()
    if spec == "African" : 
        assert True
    else: 
        assert False
        

def test_zona_African():
    zona = bCrocodil.zona_African()
    if zona == "Madagascar" :
        assert True
    else: 
        assert False

def test_clasificare_African():
    clas = bCrocodil.clasificare_African()
    if clas == "carnivor" :
        assert True
    else: 
        assert False 
