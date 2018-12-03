# _*_ coding: utf-8 _*_
from framework.base_page import BasePage

class HomePage(BasePage):
    login_btn = "link_text=>登录"
    login_username = "id=>lgin_username"
    login_phone = "id=>lgin_phone"
    login_msgcode = "id=>lgin_msgcode"
    login_idcard = "id=>lgin_idcard"
    login_button = "xpath=>//*/form/div[5]/div/button"
    login_btn_confirm = "xpath=>//*/div[11]//button"
    login_welcome = "xpath=>//*[@class='loginState__l']"



    def click_login(self):
        self.click(self.login_btn)
        self.sleep(2)

    def input_username(self,username):
        self.type(self.login_username,username)

    def input_phone(self,phone):
        self.type(self.login_phone,phone)

    def input_msgcode(self,msgcode):
        self.type(self.login_msgcode,msgcode)

    def input_idcard(self,idcard):
        self.type(self.login_idcard,idcard)

    def click_login_button(self):
        self.click(self.login_button)
        self.sleep(2)

    def click_confirm_button(self):
        self.click(self.login_btn_confirm)
        self.sleep(2)

    def loginsucess(self):
        return  self.get_text(self.login_welcome)


