import pytest
from pages.blog import blog_c

@pytest.mark.smoke
def test_blog1(page):
    blogc=blog_c(page)
    blogc.blog_click()
