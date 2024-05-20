import librarie.biblioteca_vultur as bvultur

def test_specie_vultur():
    spec = bvultur.specie_vultur()
    if spec == "vultur" : 
        assert True
    else: 
        assert False
        

def test_zona_vultur():
    zona = bvultur.zona_vultur()
    if zona == "Romania" :
        assert True
    else: 
        assert False

def test_clasificare_vultur():
    clasificare = bvultur.clasificare_vultur()
    if clasificare == "vanator" :
        assert True
    else: 
        assert False
        
        
def test_specie_plesuv():
    spec = bvultur.specie_plesuv()
    if spec == "plesuv" : 
        assert True
    else: 
        assert False
        

def test_zona_plesuv():
    zona = bvultur.zona_plesuv()
    if zona == "Europa" :
        assert True
    else: 
        assert False

def test_clasificare_plesuv():
    clas = bvultur.clasificare_plesuv()
    if clas == "zburator" :
        assert True
    else: 
        assert False  
