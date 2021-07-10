# -*- coding: utf-8 -*-
# @Time    : 2021/05/07 14:50
# @Author  : 
import time
from playwright.sync_api import sync_playwright


def run(playwright):
    browser = playwright.chromium.launch(headless=False, )
    # context = browser.contexts
    # Open new page
    page = browser.new_page()

    page.goto("https://www.baidu.com/")

    page.fill('input#kw', 'test search')
    
    page.click('input#su')
    
    time.sleep(10)
    links = page.query_selector_all('h3 a')
    
    
    for link in links:
        print(link.get_attribute('href'))

    # page.fill('input[name="wd"]', 'jingdong')

    # page.click('Text = "Jingdong"')

    
    # Current page content
    # html = page.content()
    # with page.expect_navigation():
    #    with page.expect_popup() as popup_info:
    #        # Normalize-Space This method can remove the front and rear spaces and carries with the text in the text.
    #        page.click("//a[normalize-space (.)= 'Jingdong JD.com official website How quickly, the province is only for quality life']")
    # popup_info.value

    time.sleep(10)
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

