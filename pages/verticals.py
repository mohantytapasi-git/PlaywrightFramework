from conftest import page

class vertical:
    def __init__(self,page):
        self.page=page
        self.ver=page.locator('(//a[text()="Verticals"])[1]')
        

# VERTICALS
        self.vt_trading=page.locator('//li[@data-id="trading"]')
        self.vt_retail=page.locator('//li[@data-id="retailEcommerce"]')
        self.vt_health=page.locator('//li[@data-id="healthcare"]')
        self.vt_fintech=page.locator('//li[@data-id="fintech"]')
        self.vt_customapp=page.locator('//li[@data-id="customApp"]')

#   Sub-menu items under Trading
        self.vt_stock=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.vt_paper=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.vt_cfd=page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.vt_app=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.vt_algo=page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.vt_cust=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.vt_web=page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')

# submenu under Retail and E-Commerce
        #self.vt_ecomm_dev=page.locator('(//a[@href="https://www.tranktechnolgies.com/ecommerce-web-development-company"])[2]')
        #self.vt_ecomm_app=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
        self.vt_ecomm_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        self.vt_ecomm_app=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')

#  submenu under Healthcare
        self.vt_hc=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.vt_hc_track=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')

#  submenu under Fintech
        self.vt_fin_pos=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.vt_fin_crypto=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')

#  submenu under Custom App
        self.vt_cust_desk=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.vt_cust_hrm=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.vt_cust_travel=page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.vt_cust_dating=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.vt_cust_crm_usa=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
        self.vt_cust_crm=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.vt_cust_erp=page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.vt_cust_elearn=page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.vt_cust_est=page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
   
# List Defined
        self.verticals_lst=[self.vt_stock,self.vt_paper,self.vt_cfd,self.vt_app,self.vt_algo,self.vt_cust,self.vt_web]
        self.list_ecomm=[self.vt_ecomm_dev,self.vt_ecomm_app]
        self.list_hc=[self.vt_hc,self.vt_hc_track]
        self.list_fin=[self.vt_fin_pos,self.vt_fin_crypto]
        self.list_cust_app=[self.vt_cust_desk,self.vt_cust_hrm,self.vt_cust_travel,self.vt_cust_dating,self.vt_cust_crm_usa,self.vt_cust_crm,self.vt_cust_erp,self.vt_cust_elearn,self.vt_cust_est]

    def verical_nav(self):
        for i in self.verticals_lst:
            self.ver.hover()
            self.vt_trading.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
        
    def verical_retail(self):
        for i in self.list_ecomm:
            self.ver.hover()
            self.vt_retail.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back() 
        
    def verical_healthcare(self):
        for i in self.list_hc:
            self.ver.hover()
            self.vt_health.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def verical_fintech(self):
        for i in self.list_fin:
            self.ver.hover()
            self.vt_fintech.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def vertical_cust(self):   
        for i in self.list_cust_app:
            self.ver.hover()
            self.vt_customapp.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

