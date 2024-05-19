import librarie.biblioteca_arici as libArici

def test_specie_arici():
    spec = libArici.specie_arici()
    if spec == "arici" : 
        assert True
    else: 
        assert False
        

def test_zona_arici():
    zona = libArici.zona_arici()
    if zona == "munte" :
        assert True
    else: 
        assert False

def test_clasificare_arici():
    clasificare = libArici.clasificare_arici()
    if clasificare == "de casa" :
        assert True
    else: 
        assert False
        
        
def test_specie_african():
    spec = libArici.specie_african()
    if spec == "african" : 
        assert True
    else: 
        assert False
        

def test_zona_african():
    zona = libArici.zona_african()
    if zona == "Africa" :
        assert True
    else: 
        assert False

def test_clasificare_african():
    clas = libArici.clasificare_african()
    if clas == "salbatic" :
        assert True
    else: 
        assert False  
