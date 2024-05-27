import librarie.biblioteca_cangur as bcangur

def test_specie_cangur():
    spec = bcangur.specie_cangur()
    if spec == "australian" : 
        assert True
    else: 
        assert False
        

def test_zona_cangur():
    zona = bcangur.zona_cangur()
    if zona == "Australia" :
        assert True
    else: 
        assert False

def test_clasificare_cangur():
    clasificare = bcangur.clasificare_cangur()
    if clasificare == "ierbivor" :
        assert True
    else: 
        assert False
        

