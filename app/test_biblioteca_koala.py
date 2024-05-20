import librarie.biblioteca_koala as bkoala

def test_specie_koala():
    spec = bkoala.specie_koala()
    if spec == "koala" : 
        assert True
    else: 
        assert False
        

def test_zona_koala():
    zona = bkoala.zona_koala()
    if zona == "Australia" :
        assert True
    else: 
        assert False

def test_clasificare_koala():
    clasificare = bkoala.clasificare_koala()
    if clasificare == "nu de treaba" :
        assert True
    else: 
        assert False
        
        
def test_specie_australian():
    spec = bkoala.specie_australian()
    if spec == "australian" : 
        assert True
    else: 
        assert False
        

def test_zona_australian():
    zona = bkoala.zona_australian()
    if zona == "Australia" :
        assert True
    else: 
        assert False

def test_clasificare_australian():
    clas = bkoala.clasificare_australian()
    if clas == "de treaba" :
        assert True
    else: 
        assert False  
