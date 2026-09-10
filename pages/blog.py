from conftest import page

class blog_c:
    def __init__(self,page):
        self.page=page
        self.blog=page.locator('(//a[text()="Blog"])[1]')

    #  Blog
       
        self.app_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/app-development/"])[2]')
        self.cont_mark=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/content-marketing/"])[1]')
        self.digi_mark=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/digital-marketing/"])[1]')
        self.email_mark=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/email-marketing/"])[1]')
        self.soft_it=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/software-it-company/"])[1]')
        self.ui_ux=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ui-ux-design/"])[5]')
        self.art_int=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/artificial-intelligence/"])[1]')
        self.crm_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/crm-development/"])[1]')
        self.ecomm_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ecommerce-development/"])[5]')
        self.graph_design=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/graphic-design/"])[3]')
        self.soft_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/software-development/"])[1]')
        self.web_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/web-development/"])[5]')

        self.ls_blog=[self.app_dev,self.cont_mark,self.digi_mark,self.email_mark,self.soft_it,self.ui_ux,self.art_int,self.crm_dev,self.ecomm_dev,self.graph_design,self.soft_dev,self.web_dev]

    def blog_click(self):
        for i in self.ls_blog:
            self.blog.click()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()