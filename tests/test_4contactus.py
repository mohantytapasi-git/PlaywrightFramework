import pytest
from pages.contactus import contact_us

@pytest.mark.smoke
def test_contact(page):
    cont=contact_us(page)
    cont.contactus_fill()