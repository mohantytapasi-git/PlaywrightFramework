import pytest
from pages.technologies import technology

@pytest.mark.smoke
def test_ecommdev(page):
    ecommdev=technology(page)
    ecommdev.tech_ecomm_nav()

@pytest.mark.smoke
def test_mobiles(page):
    mobile=technology(page)
    mobile.tech_mob()



