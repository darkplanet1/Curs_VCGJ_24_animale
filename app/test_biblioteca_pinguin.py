def test_specie_magellan():
    cul = b_animale.specie_magellan()
    if cul == 'Magellan':
        assert True
    else:
        assert False

def test_zona_magellan():
    cul = b_animale.zona_magellan()
    if cul == 'America de Sud':
        assert True
    else:
        assert False

def test_detalii_magellan():
    cul = b_animale.detalii_magellan()
    if cul == '70 cm inaltime':
        assert True
    else:
        assert False





def test_specie_gentoo():
    cul = b_animale.specie_gentoo()
    if cul == 'Gentoo':
        assert True
    else:
        assert False

def test_zona_gentoo():
    cul = b_animale.zona_gentoo()
    if cul == 'Peninsula Antartica':
        assert True
    else:
        assert False

def test_detalii_gentoo():
    cul = b_animale.detalii_gentoo()
    if cul == '90 cm inaltime':
        assert True
    else:
        assert False

