def test_01():
    assert 10 * 100 == 900 + 100
    assert 10 * 100 != 900 - 100


def test_02():
    assert 10 / 100 != 'sdf'
    assert 10 * 100 == 900 + 100


def test_03():
    assert 10 / 100 != 'sdf'
    assert 10 * 100 == 900 + 100


def test_04():
    assert 10 / 100 != 'sdf'
    assert 10 * 100 != 900 + 100


def test_05():
    assert 10 / 100 != 'sdf'
    assert 10 * 100 == 900 + 100


def test_06():
    assert 10 / 100 == 'sdf'
    assert 10 * 100 == 900 + 100
