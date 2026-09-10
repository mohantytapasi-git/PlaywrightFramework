from conftest import page

class contact_us:
    def __init__(self,page):
        self.page=page
        self.contact_us=page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')

    #  Contact Us      
        
        self.contact_us_name=page.locator('(//input[@placeholder="Your Name"])[2]')
        self.contact_us_mail=page.locator('(//input[@placeholder="Your Mail"])[2]')
        self.contact_us_otp=page.locator('(//input[@placeholder="Enter OTP"])[2]')
        self.contact_us_comp=page.locator('(//input[@placeholder="Your Company"])[2]')
        self.contact_us_service=page.locator('(//select[@name="service"])[2]')
        self.contact_us_phone=page.locator('(//input[@placeholder="Your Phone"])[2]')
        self.contact_us_messg_area=page.locator('(//textarea[@placeholder="Message"])[2]')
        self.contact_us_submit=page.locator('//input[@name="contact"]')

    def contactus_fill(self):        
        self.contact_us.click()
        self.contact_us_name.fill("Tapasi")
        self.contact_us_mail.fill("abc@mail.com")
        self.contact_us_otp.fill("1234")
        self.contact_us_comp.fill("ABC")
        self.contact_us_service.select_option("Web Development")
        self.contact_us_phone.fill("78676687897")
        self.contact_us_messg_area.fill("Testing The Application")
        self.page.wait_for_load_state("load")
        self.page.go_back()