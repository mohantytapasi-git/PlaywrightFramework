from conftest import page

class technology:
    def __init__(self,page):
        self.page=page
        self.technology=page.locator('(//a[text()="Technologies"])[1]')
        

#  TECHNOLOGIES
        self.tc_ecomm_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[3]')
        self.tc_mob_app=page.locator('(//a[@href="https://www.tranktechnologies.com/mobile-app-development-company"])[1]')
        self.tc_art_int=page.locator('(//a[@href="https://www.tranktechnologies.com/artificial-intelligence-development-services-company-india"])[1]')

# submenu under EComm Development
        self.tc_dev_mag=page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.tc_dev_code=page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.tc_dev_ecomm=page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.tc_dev_nop=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.tc_dev_lara=page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.tc_dev_dru=page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
        self.tc_dev_zoom=page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
        self.tc_dev_exp=page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')
        self.tc_dev_cart=page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.tc_dev_open_cart=page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])][1]')
        self.tc_dev_word_press=page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.tc_dev_shopy=page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.tc_dev_node_js=page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.tc_dev_woo=page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.tc_dev_prest=page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.tc_dev_wix=page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.tc_dev_react=page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')

# Submenu under Mobile App Development
        self.tc_mb_react=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.tc_mb_xama=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.tc_mb_flutter=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.tc_mb_swift=page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.tc_mb_ent=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.tc_mb_kotlin=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.tc_mb_ionic=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.tc_mb_appoint=page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
        
# Artificial Intelligence no sub-menu
        self.art_inte=page.locator('(//a[@href="https://www.tranktechnologies.com/artificial-intelligence-development-services-company-india"])[1]')



# Lists defined under Constructors   
        self.list_tc_ecommdev=[self.tc_dev_mag,self.tc_dev_code,self.tc_dev_ecomm,self.tc_dev_nop,self.tc_dev_lara,self.tc_dev_dru,self.tc_dev_zoom,self.tc_dev_exp,self.tc_dev_cart,self.tc_dev_word_press,self.tc_dev_word_press,self.tc_dev_shopy,self.tc_dev_node_js,self.tc_dev_woo,self.tc_dev_prest,self.tc_dev_wix,self.tc_dev_react]
        self.ls_tc_mobile=[self.tc_mb_react,self.tc_mb_xama,self.tc_mb_flutter,self.tc_mb_swift,self.tc_mb_ent,self.tc_mb_kotlin,self.tc_mb_ionic,self.tc_mb_appoint]
        self.ls_art=[self.art_inte]
        

#Methods defined under Class
    def tech_ecomm_nav(self):
        for i in self.list_tc_ecommdev:
            self.technology.hover()
            self.tc_ecomm_dev.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def tech_mob(self):        
        for i in self.ls_tc_mobile:
            self.technology.hover()
            self.tc_mob_app.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def tech_artificial(self):
        for i in self.ls_art:
            self.technology.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
