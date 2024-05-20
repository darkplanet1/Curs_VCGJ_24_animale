import librarie.biblioteca_girafa as bgirafa

def test_specie_girafa():
    spec = bgirafa.specie_girafa()
    if spec == "girafa" : 
        assert True
    else: 
        assert False
        

def test_zona_girafa():
    zona = bgirafa.zona_girafa()
    if zona == "asia" :
        assert True
    else: 
        assert False

def test_clasificare_girafa():
    clasificare = bgirafa.clasificare_girafa()
    if clasificare == "nubiana" :
        assert True
    else: 
        assert False
        
        
def test_specie_african():
    spec = bgirafa.specie_african()
    if spec == "African" : 
        assert True
    else: 
        assert False
        

def test_zona_african():
    zona = bgirafa.zona_african()
    if zona == "Africa" :
        assert True
    else: 
        assert False

def test_clasificare_african():
    clas = bgirafa.clasificare_african()
    if clas == "Nubiana" :
        assert True
    else: 
        assert False  
