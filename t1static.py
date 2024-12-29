import requests
import requests
import math
from datetime import *
import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('c:/webdrivers/chromedriver.exe')
driver.maximize_window()



#Kucoin Account Details
user_name = ''
password = ''
trading_password = ''

driver.get('https://futures.kucoin.com')

time.sleep(5)
                                         
login_btn = driver.find_element('xpath','//*[@id="root"]/div/section/header/div/div/div[2]/ul/li[4]')
login_btn.click()

time.sleep(2)

user_input = driver.find_element('xpath','/html/body/div[2]/div[3]/div[2]/div/div[1]/div/div[3]/form/div[1]/div[1]/input')
user_input.send_keys(user_name)

password_input = driver.find_element('xpath','/html/body/div[2]/div[3]/div[2]/div/div[1]/div/div[3]/form/div[2]/div[1]/input')
password_input.send_keys(password)

login_confirm = driver.find_element('xpath','/html/body/div[2]/div[3]/div[2]/div/div[1]/div/div[3]/form/button/span[1]')
login_confirm.click()

input("Login and Press Enter ...")




#Telegram Details
bot_token = ''
channel_id = ''

kucoin_client_id = ""
api_key = ""
api_secret = ""
api_passphrase = ""

phone = ""

capital = 100



'''now = int(time.time() * 1000)
str_to_sign = str(now) + 'GET' + '/api/v1/orders/'
signature = base64.b64encode(hmac.new(api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())



#Open Position
post_address = "https://futures.kucoin.com/api/v1/orders/"
post_data = {
    "clientOid": kucoin_client_id,
    "leverage": 10,
    "side": "sell",
    "size": 0.001*20,
    "symbol": 'XBTUSDTM ',
    "type": "market",
}

headers = {
    "KC-API-SIGN": signature,
    "KC-API-TIMESTAMP": str(now),
    "KC-API-KEY": api_key,
    "KC-API-PASSPHRASE": api_passphrase,
    "KC-API-KEY-VERSION": "2"
}


response = requests.post(post_address,params=post_data,headers=headers)


sdfsdf'''

crypto_list = ['BTC','ETH']
crypto_list = ['BTC','BTC']


#TakeProfit / StopLoss / Leverage
tp_number = 0.5
risk_free_number = 0.25
sl_number = 0.05
leverage_number = "8"




#Open Position ----> 0 : no position / 1 : open position
open_position_status = {'BTC':0,'ETH':0}
open_position_type = {'BTC':0,'ETH':0} # 0 Buy / 1 Sell
open_position_price = {'BTC':0,'ETH':0}
open_position_id = {'BTC':0,'ETH':0}

#Tp&Sl list
take_profit_list = {'BTC':0,'ETH':0}
stop_loss_list = {'BTC':0,'ETH':0}




#Candle Color
def candle_color(o,h,l,c):
    
    #Detect Candle
    if (h - c) < (h - o):
        candle_body = "green"
    else:
        candle_body = "red"

    return candle_body

true_position = 0
false_position = 0

sms_status_23 = False


    
while True:

    if datetime.datetime.now().hour == 23 and sms_status_23 == False:

        message = 'Finock Report\nPositive Positions is :'+str(true_position)+'\nNegetive Positions is :'+str(false_position)
    
        api_key = ""
        sms_site = ""

        sms_site0 = ""
        response = requests.post(sms_site0)
        
        true_position = 0
        false_position = 0

        sms_status_23 = True

    if datetime.datetime.now().hour == 1:
        sms_status_23 = False
        

    


    
    for crypto_name in crypto_list:


            


        
            
        #try:

        try:
            url_trend = "https://api.kucoin.com/api/v1/market/candles?symbol="+str(crypto_name)+"-USDT&type=30min"
            url_entry = "https://api.kucoin.com/api/v1/market/candles?symbol="+str(crypto_name)+"-USDT&type=1min"
            
            response_trend = requests.get(url_trend)
            response_entry = requests.get(url_entry)
            

            data = response_trend.json()
            data = data['data']
            
            data2 = response_entry.json()
            data2 = data2['data']
        except:
            continue


        

        #Trnd Detection

        close_price_list_30 = []
        for h in data:
            close_price = h[2]
            close_price_list_30.append(float(close_price))


        
        trend_price = 0
        for n in range(0,200):
            trend_price = trend_price + close_price_list_30[n]
            
        ma200 = trend_price / 200

        

        #print("0")

        if len(data2) < 700:
            continue

        #print("1")

        

        open_price_list = []
        close_price_list = []
        high_price_list = []
        low_price_list = []
        for x in data2:
            open_price = x[1]
            close_price = x[2]
            high_price = x[3]
            low_price = x[4]

            open_price_list.append(float(open_price))
            close_price_list.append(float(close_price))
            high_price_list.append(float(high_price))
            low_price_list.append(float(low_price))

        trend_direction = "long"
        if close_price_list[0] < ma200:
            trend_direction = "short"

        #print(trend_direction)
            


        




        swing_high_index = 0
        swing_high_price = 0

        swing_low_index = 0
        swing_low_price = 0

        signal_status = 4

        #print(time_frame)
        #print(high_price_list[9])
        #print("------------------------------")
        #Identify Swing and Calculate Fibo
        for a in range(10,300):

            current_time = datetime.datetime.now().hour
            

            #print("a0")

            

            if high_price_list[a-1] < high_price_list[a] and high_price_list[a-2] < high_price_list[a] and high_price_list[a-3] < high_price_list[a] and high_price_list[a-4] < high_price_list[a] and high_price_list[a-5] < high_price_list[a] and high_price_list[a-6] < high_price_list[a] and high_price_list[a-7] < high_price_list[a] and high_price_list[a-8] < high_price_list[a] and high_price_list[a-9] < high_price_list[a] and high_price_list[a-10] < high_price_list[a]:
                if high_price_list[a+1] < high_price_list[a] and high_price_list[a+2] < high_price_list[a] and high_price_list[a+3] < high_price_list[a] and high_price_list[a+4] < high_price_list[a] and high_price_list[a+5] < high_price_list[a] and high_price_list[a+6] < high_price_list[a] and high_price_list[a+7] < high_price_list[a] and high_price_list[a+8] < high_price_list[a] and high_price_list[a+9] < high_price_list[a] and high_price_list[a+10] < high_price_list[a]:


                    
                    for x in range(3,a):
                        if high_price_list[x] > high_price_list[a]:
                            signal_status = 0
                            break

                    if x < a-2:
                        break
                    #print("a1")

                    candle_a_color = candle_color(open_price_list[a],high_price_list[a],low_price_list[a],close_price_list[a])
                    if candle_a_color == "green":
                        if high_price_list[1] > close_price_list[a] or high_price_list[2] > close_price_list[a]:
                            time.sleep(0)
                        else:
                            continue
                    else:
                        if high_price_list[1] > open_price_list[a] or high_price_list[2] > open_price_list[a]:
                            time.sleep(0)
                        else:
                            continue
                        


                        
                    if signal_status == 0:
                        break

                    #print("a2")


                    if high_price_list[1] > low_price_list[a]:
                        time.sleep(1)
                    else: 
                        continue

                    position_checkout = False

                    #print("A")


                    if crypto_name == 'BTC':
                        driver.get('https://www.bybit.com/trade/usdt/BTCUSDT')
                    else:
                        driver.get('https://www.bybit.com/trade/usdt/ETHUSDT')

                    time.sleep(5)



                    ''' ---------------------------- '''


                    '''#Check Trend
                    if trend_direction != "short":
                        break'''

                    #Check Candle

                    #Engulf
                    if close_price_list[1] < low_price_list[2]:
                        print("Engulf")
                        
                    #PinBar
                    elif ((high_price_list[1] - close_price_list[1])*2) < (close_price_list[1] - low_price_list[1]) or ((high_price_list[2] - close_price_list[2])*2) < (close_price_list[2] - low_price_list[2]):
                        print("PinBar")
                    #InsideBar
                    elif high_price_list[1] < high_price_list[2] and low_price_list[1] > low_price_list[2]:
                        print("InsideBar")
                    #OutsideBar
                    elif high_price_list[1] > high_price_list[2] and low_price_list[1] < low_price_list[2]:
                        print("OutsideBar")
                    
                    else:
                        time.sleep(130)
                        break

                    print(datetime.datetime.now().hour)
                    print(datetime.datetime.now().minute)

                    '''if open_position[crypto_name] == 0:
                        open_position[crypto_name] = 1
                    else:
                        break'''
        

                    ''' ---------------------------- '''

                    #Entry Price
                    position_entry_price = close_price_list[1]
                    

                    #StopLoss
                    position_stop_loss = position_entry_price + ((position_entry_price / 100) * sl_number)

                    #tp1
                    tp1 = position_entry_price - ((position_entry_price / 100) * risk_free_number)

                    #TakeProfit
                    position_take_profit = position_entry_price - ((position_entry_price / 100) * tp_number)

                    #PositionSize
                    position_size = capital * 10

                    if crypto_name == "BTC":
                        symbol = "BTUSDT"
                    else:
                        symbol = "ETHUSDT"
                        

                    #Open Position

                    for n in range(1,3):
                        driver.refresh()
                        time.sleep(3)

                        while True:
                            try:
                                #market option                                
                                market_option = driver.find_element('xpath','//*[@id="root"]/div/section/main/section/main/div/div[2]/div/div[3]/form/div[2]/div[3]/span')
                                time.sleep(2)
                                market_option.click()

                                #position size                        
                                margin = driver.find_element('xpath','//*[@id="root"]/div/section/main/section/main/div/div[2]/div/div[3]/form/div[3]/div[3]/button[2]/span[1]') #half_margin
                                #margin = driver.find_element('xpath','//*[@id="root"]/div/section/main/section/main/div/div[2]/div/div[3]/form/div[3]/div[3]/button[4]/span[1]') #full_margin
                                
                                margin.click()

                                #leverage option                           
                                leverage_option = driver.find_element('xpath','//*[@id="root"]/div/section/main/section/main/div/div[2]/div/div[3]/form/div[4]/div[2]/i')
                                leverage_option.click()

                                #leverage_input                             
                                leverage_input = driver.find_element('xpath','//*[@id="root"]/div/section/main/section/main/div/div[2]/div/div[3]/form/div[4]/div[3]/div/div[1]/div/input')
                                leverage_input.click()

                                leverage_input.send_keys(Keys.CONTROL, 'a')

                                #enter leverage
                                leverage_input.send_keys(leverage_number)

                                #leverage confirm
                                leverage_confirm = driver.find_element('xpath','//*[@id="root"]/div/section/main/section/main/div/div[2]/div/div[3]/form/div[4]/div[3]/div/div[2]/button[2]')
                                time.sleep(1)
                                leverage_confirm.click()
                                
                                break
                            except Exception as e:
                                driver.refresh()
                                time.sleep(5)
                                print(e)
                        

                        ent_position_status = 0

                        #Short Position                                         
                        short_position = driver.find_element('xpath','//*[@id="root"]/div/section/main/section/main/div/div[2]/div/div[3]/form/div[6]/div/div[2]/button')
                        time.sleep(1)
                        short_position.click()

                        try:
                            time.sleep(1)
                            trading_password_element = driver.find_element('xpath','//*[@id="mui-79081"]/div/div/div[4]/div[2]/button[1]')
                            time.sleep(2)
                            #trading_password_element.send_keys(Keys.CONTROL, 'a')
                            time.sleep(1)
                            trading_password_element.send_keys(trading_password)

                            confirm_tpassword = driver.find_element('xpath','/html/body/div[5]/div[3]/div[3]/button')
                            time.sleep(1)
                            confirm_tpassword.click()
                            
                        except:
                            time.sleep(0)
                        


                        
                        
                                
                        
                        

                        ''' ---------------------------- '''



                        print(a)
                        message = "Sell Position "+str(crypto_name) + " in "+str(position_entry_price)

                        position_direction = "sell"
                        
                        '''api_key = ""
                        sms_site = ""

                        sms_site0 = ""
                        response = requests.post(sms_site0)'''

                        print(message)
                        print("-----------------------------")
                        signal_status = 1

                        driver.refresh()
                        time.sleep(3)
                        html = driver.find_element_by_tag_name('html')
                        html.send_keys(Keys.END)

                        time.sleep(2)

                        for x in range(1,4):
                            try:
                                #Close_Position  
                                close_position = driver.find_element('xpath','//*[@id="root"]/div/section/main/section/main/div/div[1]/div[3]/div[5]/section/div/div/div[3]/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[12]/div/button[2]/span[1]')
                                time.sleep(1)
                                position_checkout = True
                                
                                break
                            except: 
                                continue

                        if x < 3:
                            break
                            


                    if position_checkout == False:
                        break
                    

                    #Close Position
                    while True:

                        

                        try:

                            check_price = "https://api.kucoin.com/api/v1/market/candles?symbol="+str(crypto_name)+"-USDT&type=1min"

                            response_check_price = requests.get(check_price)
                            

                            data = response_check_price.json()
                            data = data['data']
                            


                            close_price_list = []
                            for h in data:
                                close_price = h[3]
                                close_price_list.append(float(close_price))

                            high_price_list = []
                            for h in data:
                                high_price = h[3]
                                high_price_list.append(float(high_price))

                            low_price_list = []
                            for h in data:
                                low_price = h[4]
                                low_price_list.append(float(low_price))

                        except:
                            continue


                        #Risk Free & Close Position

                        if position_direction == "sell":



                            if close_price_list[0] > position_stop_loss:
                                time.sleep(0)
                                false_position = false_position + 1
                                
                            elif close_price_list[0] < position_take_profit:
                                time.sleep(0)
                                true_position = true_position + 1

                            elif close_price_list[0] < tp1:
                                position_stop_loss = position_entry_price
                                continue
                                
                            else:
                                continue
                            
                        else:

                            if high_price_list[0] > tp1:
                                position_stop_loss = position_entry_price
                                continue

                            if high_price_list[0] > position_take_profit:
                                time.sleep(0)
                                true_position =  true_position + 1
                                
                            elif low_price_list[0] < position_stop_loss:
                                time.sleep(0)
                                false_position = false_position + 1
                                
                            else:
                                continue



                            




                            
                        counter = 0
                        while True:
                            try:
                                #Close_Position  
                                close_position = driver.find_element('xpath','//*[@id="root"]/div/section/main/section/main/div/div[1]/div[3]/div[5]/section/div/div/div[3]/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[12]/div/button[2]/span[1]')            
                                time.sleep(1)
                                close_position.click()
                                break
                            except:
                                if counter > 3:
                                    break
                                counter = counter + 1
                                continue
                        
                        if counter >= 3:
                            break


                        try:
                            time.sleep(1)
                            trading_password_element = driver.find_element('xpath','//*[@id="mui-79081"]/div/div/div[4]/div[2]/button[1]')
                            time.sleep(2)
                            #trading_password_element.send_keys(Keys.CONTROL, 'a')
                            time.sleep(1)
                            trading_password_element.send_keys(trading_password)

                            confirm_tpassword = driver.find_element('xpath','/html/body/div[5]/div[3]/div[3]/button')
                            time.sleep(1)
                            confirm_tpassword.click()
                            
                        except:
                            time.sleep(0)

                        time.sleep(2)
                        full_size = driver.find_element('xpath','/html/body/div[2]/div[3]/div/div[2]/div/div[2]/form/div[2]/div/button[4]/span[1]')
                        time.sleep(2)
                        full_size.click()

                        try:
                            time.sleep(1)
                            trading_password_element = driver.find_element('xpath','//*[@id="mui-79081"]/div/div/div[4]/div[2]/button[1]')
                            time.sleep(2)
                            #trading_password_element.send_keys(Keys.CONTROL, 'a')
                            time.sleep(1)
                            trading_password_element.send_keys(trading_password)

                            confirm_tpassword = driver.find_element('xpath','/html/body/div[5]/div[3]/div[3]/button')
                            time.sleep(1)
                            confirm_tpassword.click()
                            
                        except:
                            time.sleep(0)


                        close_confirm = driver.find_element('xpath','/html/body/div[2]/div[3]/div/div[2]/div/div[2]/form/div[3]/button[2]/span[1]')
                        time.sleep(2)
                        close_confirm.click()

                        try:
                            time.sleep(1)
                            trading_password_element = driver.find_element('xpath','//*[@id="mui-79081"]/div/div/div[4]/div[2]/button[1]')
                            time.sleep(2)
                            #trading_password_element.send_keys(Keys.CONTROL, 'a')
                            time.sleep(1)
                            trading_password_element.send_keys(trading_password)

                            confirm_tpassword = driver.find_element('xpath','/html/body/div[5]/div[3]/div[3]/button')
                            time.sleep(1)
                            confirm_tpassword.click()
                            
                        except:
                            time.sleep(0)

                        message = "Close Sell Position "+str(crypto_name) + " in "+str(close_price_list[0])
                        print(message)
                    

                            
                        time.sleep(130)
                        break
                        
                        
                    break
                

                else:
                    signal_status = 2
                    break
    
            elif low_price_list[a-1] > low_price_list[a] and low_price_list[a-2] > low_price_list[a] and low_price_list[a-3] > low_price_list[a] and low_price_list[a-4] > low_price_list[a] and low_price_list[a-5] > low_price_list[a] and low_price_list[a-6] > low_price_list[a] and low_price_list[a-7] > low_price_list[a] and low_price_list[a-8] > low_price_list[a] and low_price_list[a-9] > low_price_list[a] and low_price_list[a-10] > low_price_list[a]:
                if low_price_list[a+1] > low_price_list[a] and low_price_list[a+2] > low_price_list[a] and low_price_list[a+3] > low_price_list[a] and low_price_list[a+4] > low_price_list[a] and low_price_list[a+5] > low_price_list[a] and low_price_list[a+6] > low_price_list[a] and low_price_list[a+7] > low_price_list[a] and low_price_list[a+8] > low_price_list[a] and low_price_list[a+9] > low_price_list[a] and low_price_list[a+10] > low_price_list[a]:

                    #print("b0")


                
                    for x in range(3,a):
                        if low_price_list[x] < low_price_list[a]:
                            signal_status = 0
                            break

                    if x < a-2:
                        break

                    candle_a_color = candle_color(open_price_list[a],high_price_list[a],low_price_list[a],close_price_list[a])
                    if candle_a_color == "green":
                        if low_price_list[1] < open_price_list[a] or low_price_list[2] < open_price_list[a]:
                            time.sleep(0)
                        else:
                            continue
                    else:
                        if low_price_list[1] < close_price_list[a] or low_price_list[2] < close_price_list[a]:
                            time.sleep(0)
                        else:
                            continue

                        
                    if signal_status == 0:
                        break

                    #print("b1")

                    if low_price_list[1] < high_price_list[a]:
                        time.sleep(1)
                    else: 
                        continue

                    #print("B")

                    position_checkout = False

                    

                    if crypto_name == 'BTC':
                        driver.get('https://www.bybit.com/trade/usdt/BTCUSDT')
                    else:
                        driver.get('https://www.bybit.com/trade/usdt/ETHUSDT')


                    time.sleep(5)


                    ''' ---------------------------- '''


                    '''#Check Trend
                    if trend_direction != "long":
                        break'''

                    #Check Candle

                    #Engulf
                    if close_price_list[1] > high_price_list[2]:
                        print("Engulf")
                        
                    #PinBar
                    elif ((close_price_list[1] - low_price_list[1])*2) < (high_price_list[1] - close_price_list[1]) or ((close_price_list[2] - low_price_list[2])*2) < (high_price_list[2] - close_price_list[2]):
                        print("PinBar")
                    #InsideBar
                    elif high_price_list[1] < high_price_list[2] and low_price_list[1] > low_price_list[2]:
                        print("InsideBar")
                    #OutsideBar
                    elif high_price_list[1] > high_price_list[2] and low_price_list[1] < low_price_list[2]:
                        print("OutsideBar")
                    
                    else:
                        time.sleep(130)
                        break

                    print(datetime.datetime.now().hour)
                    print(datetime.datetime.now().minute)

                    '''if open_position[crypto_name] == 0:
                        open_position[crypto_name] = 1
                    else:
                        break'''
        

                    ''' ---------------------------- '''

                    #Entry Price
                    position_entry_price = close_price_list[1]
                    

                    #StopLoss
                    position_stop_loss = position_entry_price - ((position_entry_price / 100) * sl_number)

                    #tp1
                    tp1 = position_entry_price + ((position_entry_price / 100) * risk_free_number)

                    #TakeProfit
                    position_take_profit = position_entry_price + ((position_entry_price / 100) * tp_number)

                    #PositionSize
                    position_size = capital * 10

                    if crypto_name == "BTC":
                        symbol = "XBTUSDM"
                    else:
                        symbol = "ETHUSDM"
                        

                    #Open Position
                            
                    for n in range(1,4):
                        driver.refresh()
                        time.sleep(3)

                        while True:
                            try:
                                #market option
                                market_option = driver.find_element('xpath','//*[@id="root"]/div/section/main/section/main/div/div[2]/div/div[3]/form/div[2]/div[3]/span')
                                time.sleep(2)
                                market_option.click()

                                #position size
                                margin = driver.find_element('xpath','//*[@id="root"]/div/section/main/section/main/div/div[2]/div/div[3]/form/div[3]/div[3]/button[2]/span[1]') #half_margin
                                #margin = driver.find_element('xpath','//*[@id="root"]/div/section/main/section/main/div/div[2]/div/div[3]/form/div[3]/div[3]/button[4]/span[1]') #full_margin
                                
                                margin.click()

                                #leverage option
                                leverage_option = driver.find_element('xpath','//*[@id="root"]/div/section/main/section/main/div/div[2]/div/div[3]/form/div[4]/div[2]/i')
                                leverage_option.click()

                                #leverage_input
                                leverage_input = driver.find_element('xpath','//*[@id="root"]/div/section/main/section/main/div/div[2]/div/div[3]/form/div[4]/div[3]/div/div[1]/div/input')
                                leverage_input.click()

                                leverage_input.send_keys(Keys.CONTROL, 'a')

                                #enter leverage
                                leverage_input.send_keys(leverage_number)

                                #leverage confirm
                                leverage_confirm = driver.find_element('xpath','//*[@id="root"]/div/section/main/section/main/div/div[2]/div/div[3]/form/div[4]/div[3]/div/div[2]/button[2]')
                                time.sleep(1)
                                leverage_confirm.click()

                                break
                            except Exception as e:
                                driver.refresh()
                                time.sleep(3)
                                print(e)


                        ent_position_starus = 0

                        #Long Position                               
                        long_position = driver.find_element('xpath','//*[@id="root"]/div/section/main/section/main/div/div[2]/div/div[3]/form/div[6]/div/div[1]/button')
                        time.sleep(1)
                        long_position.click()


                        try:
                            time.sleep(1)
                            trading_password_element = driver.find_element('xpath','//*[@id="mui-79081"]/div/div/div[4]/div[2]/button[1]')
                            time.sleep(2)
                            #trading_password_element.send_keys(Keys.CONTROL, 'a')
                            time.sleep(1)
                            trading_password_element.send_keys(trading_password)

                            confirm_tpassword = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div[3]/button')
                            time.sleep(1)
                            confirm_tpassword.click()
                            
                        except:
                            time.sleep(0)
                                
                        
                        

                        ''' ---------------------------- '''



                        print(a)
                        message = "Buy Position "+str(crypto_name) + " in "+str(position_entry_price)
                        
                        ''''api_key = ""
                        sms_site = ""

                        sms_site0 = ""
                        response = requests.post(sms_site0)'''

                        print(message)
                        print("-----------------------------")
                        signal_status = 1

                        driver.refresh()
                        time.sleep(3)
                        html = driver.find_element_by_tag_name('html')
                        html.send_keys(Keys.END)

                        time.sleep(2)

                        for x in range(1,4):

                            try:
                                #Close_Position  
                                close_position = driver.find_element('xpath','//*[@id="root"]/div/section/main/section/main/div/div[1]/div[3]/div[5]/section/div/div/div[3]/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[12]/div/button[2]/span[1]')            
                                time.sleep(1)
                                position_checkout = True
                                
                                break
                            except: 
                                continue

                        
                        if x < 3:
                            break
                            
                    if position_checkout == False:
                        break

                    #Close Position
                    while True:

                        try:

                            check_price = "https://api.kucoin.com/api/v1/market/candles?symbol="+str(crypto_name)+"-USDT&type=1min"

                            response_check_price = requests.get(check_price)
                            

                            data = response_check_price.json()
                            data = data['data']
                                


                            close_price_list = []
                            for h in data:
                                close_price = h[3]
                                close_price_list.append(float(close_price))

                            high_price_list = []
                            for h in data:
                                high_price = h[3]
                                high_price_list.append(float(high_price))

                            low_price_list = []
                            for h in data:
                                low_price = h[4]
                                low_price_list.append(float(low_price))
                                

                            #Risk Free & Close Position
                            if trend_direction == "short":

                                if close_price_list[0] < tp1:
                                    position_stop_loss = position_entry_price
                                    continue

                                if close_price_list[0] > position_stop_loss:
                                    time.sleep(0)
                                    false_position = false_position + 1
                                    
                                elif close_price_list[0] < position_take_profit:
                                    time.sleep(0)
                                    true_position = true_position + 1
                                    
                                else:
                                    continue
                                
                            else:

                                if close_price_list[0] > tp1:
                                    position_stop_loss = position_entry_price
                                    continue

                                if close_price_list[0] > position_take_profit:
                                    time.sleep(0)
                                    true_position =  true_position + 1
                                    
                                elif close_price_list[0] < position_stop_loss:
                                    time.sleep(0)
                                    false_position = false_position + 1
                                    
                                else:
                                    continue

                        except:
                            continue
                            



                    

                        counter = 0
                        while True:
                            try:
                                #Close_Position  
                                close_position = driver.find_element('xpath','//*[@id="root"]/div/section/main/section/main/div/div[1]/div[3]/div[5]/section/div/div/div[3]/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[12]/div/button[2]/span[1]')            
                                time.sleep(1)
                                close_position.click()
                                break
                            except:
                                if counter > 3:
                                    break
                                counter = counter + 1
                                continue
                        
                        if counter >= 3:
                            break


                        try:
                            time.sleep(1)
                            trading_password_element = driver.find_element('xpath','//*[@id="mui-79081"]/div/div/div[4]/div[2]/button[1]')
                            time.sleep(2)
                            #trading_password_element.send_keys(Keys.CONTROL, 'a')
                            time.sleep(1)
                            trading_password_element.send_keys(trading_password)

                            confirm_tpassword = driver.find_element('xpath','/html/body/div[5]/div[3]/div[3]/button')
                            time.sleep(1)
                            confirm_tpassword.click()
                            
                        except:
                            time.sleep(0)


                        time.sleep(2)
                        full_size = driver.find_element('xpath','/html/body/div[2]/div[3]/div/div[2]/div/div[2]/form/div[2]/div/button[4]/span[1]')
                        time.sleep(2)
                        full_size.click()

                        try:
                            time.sleep(1)
                            trading_password_element = driver.find_element('xpath','//*[@id="mui-79081"]/div/div/div[4]/div[2]/button[1]')
                            time.sleep(2)
                            #trading_password_element.send_keys(Keys.CONTROL, 'a')
                            time.sleep(1)
                            trading_password_element.send_keys(trading_password)

                            confirm_tpassword = driver.find_element('xpath','/html/body/div[5]/div[3]/div[3]/button')
                            time.sleep(1)
                            confirm_tpassword.click()
                            
                        except:
                            time.sleep(0)


                        close_confirm = driver.find_element('xpath','/html/body/div[2]/div[3]/div/div[2]/div/div[2]/form/div[3]/button[2]/span[1]')
                        time.sleep(1)
                        close_confirm.click()

                        try:
                            time.sleep(1)
                            trading_password_element = driver.find_element('xpath','//*[@id="mui-79081"]/div/div/div[4]/div[2]/button[1]')
                            time.sleep(2)
                            #trading_password_element.send_keys(Keys.CONTROL, 'a')
                            time.sleep(1)
                            trading_password_element.send_keys(trading_password)

                            confirm_tpassword = driver.find_element('xpath','/html/body/div[5]/div[3]/div[3]/button')
                            time.sleep(1)
                            confirm_tpassword.click()
                            
                        except:
                            time.sleep(0)

                        

                        message = "Close Buy Position "+str(crypto_name) + " in "+str(close_price_list[0])
                        print(message)

                            
                        time.sleep(130)
                        break
                    
                                            
                                            

                    break
            break
                
        '''except Exception as e:
            print(e)
            time.sleep(3)
            continue'''

                


            


        




