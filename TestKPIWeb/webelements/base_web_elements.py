class BasePageWebElements(object):
    """[summary]
    All web elements located by xpath for base page. 
    """
    locators = {'ele_top_bar_locator_xpath': '//*[@id="root"]/div/header/header/div',
                'ele_nio_logo_locator_xpath': '//*[@id="root"]/div/header/header/div/img',
                'ele_top_left_btn_locator_xpath': '//*[@id="root"]/div/header/header/div/button',
                'ele_left_nav_bar_locator_xpath': '//*[@id="root"]/div/div/div',
                'ele_left_nav_button_elements_locator_xpath': '//nav/a',
                'ele_main_pad_locator_xpath': '//*[@id="root"]/div/main/div'}
