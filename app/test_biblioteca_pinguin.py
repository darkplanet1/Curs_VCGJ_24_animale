def test_specie_magellan():
    cul = b_pinguin.specie_magellan()
    if cul == 'Magellan':
        assert True
    else:
        assert False

def test_zona_magellan():
    cul = b_pinguin.zona_magellan()
    if cul == 'America de Sud':
        assert True
    else:
        assert False

def test_detalii_magellan():
    cul = b_pinguin.detalii_magellan()
    if cul == '70 cm inaltime':
        assert True
    else:
        assert False


