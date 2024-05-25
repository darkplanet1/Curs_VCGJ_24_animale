import librarie.biblioteca_Camila as bCamila

def test_specie_Camila():
    spec = bCamila.specie_Camila()
    if spec == "Arabian" : 
        assert True
    else: 
        assert False
        

def test_zona_Camila():
    zona = bCamila.zona_Camila()
    if zona == "Liban" :
        assert True
    else: 
        assert False

def test_clasificare_Camila():
    clasificare = bCamila.clasificare_Camila()
    if clasificare == "carnivor" :
        assert True
    else: 
        assert False
        
        
def test_specie_Arabian():
    spec = bCamila.specie_Arabian()
    if spec == "Arabian" : 
        assert True
    else: 
        assert False
        

def test_zona_Arabian():
    zona = bCamila.zona_Arabian()
    if zona == "Liban" :
        assert True
    else: 
        assert False

def test_clasificare_Arabian():
    clas = bCamila.clasificare_Arabian()
    if clas == "carnivor" :
        assert True
    else: 
        assert False  
