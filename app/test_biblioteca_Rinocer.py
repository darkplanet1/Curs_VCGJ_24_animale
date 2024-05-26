import librarie.biblioteca_Rinocer as Rinocer


def test_specie_Rinocer():
    rinocer = bRinocer
    spec = rinocer.specie_Rinocer()
    if spec == "African":
        assert True
    else:
        assert False


def test_zona_Rinocer():
    zona = bRinocer.zona_Rinocer()
    if zona == "Africa":
        assert True
    else:
        assert False


def test_clasificare_Rinocer():
    rinocer = bRinocer
    clasificare = rinocer.clasificare_Rinocer()
    if clasificare == "carnivor":
        assert True
    else:
        assert False


def test_specie_African():
    spec = bRinocer.specie_African()
    if spec == "African":
        assert True
    else:
        assert False


def test_zona_African():
    zona = bRinocer.zona_African()
    if zona == "Africa":
        assert True
    else:
        assert False


def test_clasificare_African():
    clas = bRinocer.clasificare_African()
    if clas == "carnivor":
        assert True
    else:
        assert False  
