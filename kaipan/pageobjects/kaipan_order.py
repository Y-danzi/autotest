# _*_ coding: utf-8 _*_
from framework.base_page import BasePage

class OrderPage(BasePage):
    room_id = "xpath=>//*[@room_id='75909']"
    agreement = "xpath=>//*[@onchange='agree(this);']"
    submit_addf = "xpath=>//*[@id='submit_addfavorite']"
    submit_room = "xpath=>//*[@id='roomdetail_submit']"

    def click_room(self):
        self.click(self.room_id)

    def agree(self):
        self.click(self.agreement)

    def sub_addfavorite(self):
        self.click(self.submit_addf)
        self.sleep(2)

    def sub_roomdetail(self):
        self.click(self.submit_room)
        self.sleep(2)

