import librarie.biblioteca_vulpe as bvulpe

def test_specie_vulpe_rosie():
    spec = bvulpe.specie_vulpe_rosie()
    if spec == "vulpe rosie" : 
        assert True
    else: 
        assert False
        

def test_zona_vulpe_rosie():
    zona = bvulpe.zona_vulpe_rosie()
    if zona == "in toata lumea" :
        assert True
    else: 
        assert False

def test_clasificare_vulpe_rosie():
    clasificare = bvulpe.clasificare_vulpe_rosie()
    if clasificare == "omnivor" :
        assert True
    else: 
        assert False
        
        
def test_specie_vulpe_polara():
    spec = bvulpe.specie_vulpe_polara()
    if spec == "vulpe polara" : 
        assert True
    else: 
        assert False
        

def test_zona_vulpe_polara():
    zona = bvulpe.zona_vulpe_polara()
    if zona == "in regiunile de tundra" :
        assert True
    else: 
        assert False

def test_clasificare_vulpe_polara():
    clas = bvulpe.clasificare_vulpe_polara()
    if clas == "carnivor" :
        assert True
    else: 
        assert False  
