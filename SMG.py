import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


#### Main
user_name = "NJ_41_ZZ650"
password = "PQHJ6936"
driver = webdriver.Chrome("C:\\Users\\mansfj\\Desktop\\Trading_Bot\\chromedriver_win32\\chromedriver.exe")
login(driver,user_name,password)
print("done.")


def login(driver,user_name, password):
	driver.get("https://www.stockmarketgame.org/login.html")
	#select id box
	id_box = driver.find_element_by_name('ACCOUNTNO')
	# Send id information
	id_box.send_keys(user_name)
	#select password box
	id_box = driver.find_element_by_name('USER_PIN')
	# Send password
	id_box.send_keys(password)

	# Find login button
	login_button = driver.find_element_by_class_name('button primary')
	# Click login
	login_button.click()

#buy_sell: rbBuy,rbSell,rbShortCell,rbShortCover
def buy(amount,ticker,order_type = 0,buy_sell = 'rbSell',limit_amount = 0):
	
	if amount < 10:
		print("amount must be at least 10 stocks")
		return
	elif buy_sell != 'rbSell' or buy_sell != rbBuy or buy_sell != rbShortCover or buy_sell != rbShortCell:
		print ("buy_sell type not properly configured")
		return
	elif order_type != 0 and order_type != 1:
		print ("order_type not properly configured(should be either 1 or 0)")
	driver.get("https://www.stockmarketgame.org/eat.html")

	driver.find_element_by_id('aStockTrade').click()


	driver.find_element_by_id(buy_sell).click()

	driver.find_element_by_id('SymbolName').send_keys(ticker)

	#order tpye: 1 == Market 2 == Limit
	Select(driver.find_element_by_id('OrderType')).select.select_by_value(order_type)

	driver.find_element_by_id('BuySellAmt').send_keys(amount)
	if OrderType == 1:
		driver.find_element_by_id('LimitPrice').send_keys(limit_amount)
		
	driver.find_element_by_id('btnSend').send_keys(ticker)
	driver.find_element_by_id('TradePassword').send_keys("PQHJ6936")

