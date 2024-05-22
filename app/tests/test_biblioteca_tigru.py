import librarie.biblioteca_tigru as btigru

def test_specie():
    cul = btigru.specie()
    if cul == 'Siberian':
        assert True
    else:
        assert False

def test_zona():
    cul = btigru.zona()
    if cul == 'Rusia':
        assert True
    else:
        assert False

def test_detalii():
    cul = btigru.detalii()
    if cul == 'carnivor':
        assert True
    else:
        assert False
