import librarie.biblioteca_Rechin as bRechin

def test_specie_Rechin():
    spec = bRechin.specie_Rechin()
    if spec == "European" : 
        assert True
    else: 
        assert False
        

def test_zona_Rechin():
    zona = bRechin.zona_Rechin()
    if zona == "Italy" :
        assert True
    else: 
        assert False

def test_clasificare_Rechin():
    clasificare = bRechin.clasificare_Rechin()
    if clasificare == "carnivor" :
        assert True
    else: 
        assert False
        
        
def test_specie_European():
    spec = bRechin.specie_European()
    if spec == "European" : 
        assert True
    else: 
        assert False
        

def test_zona_European():
    zona = bRechin.zona_European()
    if zona == "Italy" :
        assert True
    else: 
        assert False

def test_clasificare_European():
    clas = bRechin.clasificare_European()
    if clas == "carnivor" :
        assert True
    else: 
        assert False
