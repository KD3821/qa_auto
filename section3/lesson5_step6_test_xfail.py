import pytest

@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False


'''
параметр (strict=True) в случае неожиданного прохождения теста, помеченного как xfail, в отчете отметит его как упавший
'''