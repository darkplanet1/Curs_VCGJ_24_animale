def test_culoare_pinguin():
    cul = b_animale.culoare_pinguin()
    if cul == 'alb cu negru':
        assert True
    else:
        assert False

def test_hrana_pinguin():
    inf = b_animale.hrana_pinguin()
    if inf == 'carnivor':
        assert True
    else:
        assert False

def test_invelisul_corpului_pinguin():
    inf = b_animale.invelisul_corpului_pinguin()
    if inf == 'blana':
        assert True
    else:
        assert False
