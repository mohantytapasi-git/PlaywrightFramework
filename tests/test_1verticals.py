import pytest
from pages.verticals import vertical

@pytest.mark.smoke
def test_trading(page):
    verticals=vertical(page)
    verticals.verical_nav()

@pytest.mark.smoke
def test_retail(page):
    trading=vertical(page)
    trading.verical_retail()

@pytest.mark.smoke
def test_healtcare(page):
    healtcare=vertical(page)
    healtcare.verical_healthcare()

@pytest.mark.smoke
def test_fintech(page):
    fintech=vertical(page)
    fintech.verical_fintech()

@pytest.mark.smoke
def test_custom(page):
    custo_app=vertical(page)
    custo_app.vertical_cust()


