import librarie.biblioteca_foca as bfoca

def test_specie_foca():
    spec = bfoca.specie_foca()
    if spec == "foca" : 
        assert True
    else: 
        assert False
        

def test_zona_foca():
    zona = bfoca.zona_foca()
    if zona == "zona_polara" :
        assert True
    else: 
        assert False

def test_clasificare_foca():
    clasificare = bfoca.clasificare_foca()
    if clasificare == "inelata" :
        assert True
    else: 
        assert False
        
        
def test_specie_polara():
    spec = bfoca.specie_polara()
    if spec == "polara" : 
        assert True
    else: 
        assert False
        

def test_zona_polara():
    zona = bfoca.zona_polara()
    if zona == "Polul_Nord" :
        assert True
    else: 
        assert False

def test_clasificare_polara():
    clas = bfoca.clasificare_polara()
    if clas == "inelata" :
        assert True
    else: 
        assert False  
