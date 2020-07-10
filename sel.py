from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome("C:\Users\jay\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(1)
driver.find_element_by_id('nav-link-accountList').click()
time.sleep(1)
driver.find_element_by_xpath(".//input[@type='email']").send_keys('your_password_here')
# driver.find_element_by_name('email').send_keys('8698947144')
driver.find_element_by_xpath(".//input[@id='continue']").click()
driver.find_element_by_xpath(".//input[@type='password']").send_keys('runescape')
driver.find_element_by_xpath(".//input[@id='signInSubmit']").click()
driver.find_element_by_xpath(".//input[@id='twotabsearchtextbox']").send_keys('samsung s20')
main_window = driver.current_window_handle
time.sleep(1)
driver.find_element_by_xpath(".//input[@type='submit']").click()
#link1
# testvar=driver.find_element_by_xpath(".//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']/a[@class='a-link-normal a-text-normal']")
# print(testvar.get_attribute('text'))
driver.find_element_by_xpath(".//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']/a[@class='a-link-normal a-text-normal']").click() 

# driver.switch_to_window(main_window)
driver.switch_to.window(driver.window_handles[-1])
time.sleep(3)
# driver.find_element_by_xpath(".//input[@id='twotabsearchtextbox']").send_keys('samsung tab2')
driver.find_element_by_id("add-to-cart-button").click()
firstlink_window = driver.current_window_handle
print(driver.current_window_handle)
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div[5]/div[1]/div[11]/div/div[1]/div/div/div[1]/a").click()
driver.refresh()
driver.close()
driver.switch_to_window(main_window)
driver.refresh()
#link2
driver.find_element_by_xpath("//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div[3]/div/span/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a").click()
# driver.find_element_by_xpath("//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div[3]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span").click()
driver.switch_to.window(driver.window_handles[-1])
time.sleep(3)
driver.find_element_by_id("add-to-cart-button").click()
secondlink_window = driver.current_window_handle
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div[5]/div[1]/div[11]/div/div[1]/div/div/div[1]/a").click()
driver.refresh()
driver.close()
driver.switch_to_window(main_window)
driver.refresh()
#link 3
driver.find_element_by_xpath("//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div[4]/div/span/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a").click()
# driver.find_element_by_xpath("//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div[4]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span").click()
driver.switch_to.window(driver.window_handles[-1])
time.sleep(3)
driver.find_element_by_id("add-to-cart-button").click()
thirdlink_window = driver.current_window_handle
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div[5]/div[1]/div[11]/div/div[1]/div/div/div[1]/a").click()
driver.refresh()
driver.close()
driver.switch_to_window(main_window)
driver.refresh()
#link4
driver.find_element_by_xpath("//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div[5]/div/span/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a").click()
# driver.find_element_by_xpath("//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div[5]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span").click()
driver.switch_to.window(driver.window_handles[-1])
time.sleep(3)
driver.find_element_by_id("add-to-cart-button").click()
fourthlink_window = driver.current_window_handle
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div[5]/div[1]/div[11]/div/div[1]/div/div/div[1]/a").click()
driver.refresh()
driver.close()
driver.switch_to_window(main_window)
driver.refresh()
#link5
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div/span[3]/div[2]/div[14]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a").click()
# driver.find_element_by_xpath("//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div[8]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span").click()
driver.switch_to.window(driver.window_handles[-1])
time.sleep(3)
driver.find_element_by_id("add-to-cart-button").click()
fifthlink_window = driver.current_window_handle
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div[5]/div[1]/div[11]/div/div[1]/div/div/div[1]/a").click()
driver.refresh()
driver.close()
driver.switch_to_window(main_window)

driver.refresh()
#clicking on cart and proceeding to pay 
time.sleep(3)
driver.find_element_by_xpath("//*[@id='nav-cart']").click()
time.sleep(3)
# delete item from cart

driver.find_element_by_xpath(".//input[@id='twotabsearchtextbox']").send_keys('delete blue phone')
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[5]/div/div[2]/div[2]/form/div[2]/div[3]/div[4]/div/div[1]/div/div/div[2]/div[1]/span[2]/span/input").click()
time.sleep(4)

# proceed to buy button clicking below
driver.find_element_by_xpath("//*[@id='sc-buy-box-ptc-button']/span/input").click()
# driver.find_element_by_id('ap_email').send_keys('8698947144')
# driver.find_element_by_id('continue').click()
# driver.find_element_by_class_name('nav-line-2').click()
# element_to_hover_over=driver.find_elements_by_class_name('nav-a nav-a-2')
# hover=ActionChains(driver).move_to_element(element_to_hover_over)
# hover.click()
# driver.find_element_by_id('twotabsearchtextbox').send_keys('laptops')






# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# import time
# driver = webdriver.Chrome("C:\Users\jay\Downloads\chromedriver_win32\chromedriver.exe")
# driver.get("https://www.google.com/")
# driver.maximize_window()
# time.sleep(1)
# driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input").send_keys('continuum managed services')
# time.sleep(2)
# driver.find_element_by_xpath(".//input[@value='Google Search']").click()
# time.sleep(2)
# # driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input").send_keys(Keys.ENTER)
# # time.sleep(1)
# # driver.find_element_by_xpath("//*[@id='rso']/div[3]/div/div[1]/a/h3").click()

# driver.find_element_by_xpath("//*[@id='rso']/div[3]/div/div[1]/a/h3").click()

