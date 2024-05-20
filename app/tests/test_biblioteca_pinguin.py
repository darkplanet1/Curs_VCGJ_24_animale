import librarie.biblioteca_pinguin as bpinguin

def test_specie_magellan():
    cul = bpinguin.specie_magellan()
    if cul == 'Magellan':
        assert True
    else:
        assert False

def test_zona_magellan():
    cul = bpinguin.zona_magellan()
    if cul == 'America de Sud':
        assert True
    else:
        assert False

def test_detalii_magellan():
    cul = bpinguin.detalii_magellan()
    if cul == '70 cm inaltime':
        assert True
    else:
        assert False
