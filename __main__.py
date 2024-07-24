from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime
from time import sleep
from selenium.webdriver.common.keys import Keys
class Instagram:
    def __init__(self):
        print('Trying initiate the webdriver...')
        try: 
            self.options = Options()
            self.path_data = os.path.dirname(__file__)
            self.options.add_argument(f'--user-data-dir={self.path_data}/UserData') #Configure the path to save all the browser data.
            self.driver = webdriver.Chrome(options=self.options) #Start the WebDriver
            print('Success! Webdriver started, waiting for some action.')

            self.user_message_product = None

        except Exception as e:
            print("Failed to initiate the webdriver: \n" + e)

    def verifyNotifcatons(self):
        try: 
            url = "https://www.instagram.com/direct/inbox/"
            print("Trying to get: " + url)
            self.driver.get(url=url)
            sleep(5) #Wait the page load
            self.page_title = self.driver.title #Get the tilte of page.
            
            print(f"\n\n\n------------- Success! -------------\n\n\n")

            print(f'Page title: {self.page_title}')
            if self.page_title.startswith('('):
                self.index_first_colum = self.page_title.find('(') # -> Int value for the first parent.
                self.index_second_colum = self.page_title.find(')') # -> Int value for the second parent.
                
                self.total_of_notifications: int = self.page_title[self.index_first_colum + 1]

                print('Total of notifications: ' + self.total_of_notifications)

                return self.total_of_notifications

        except Exception as e:
            print("Error to access the inbox page. Try login, again!")
            self.driver.get('https://www.instagram.com/')
            
    def getMessage(self):
        try:
            self.notification = self.driver.find_elements(By.CSS_SELECTOR, 'span.x6s0dn4.xzolkzo.x12go9s9.x1rnf11y.xprq8jg.x9f619.x3nfvp2.xl56j7k.x1tu34mt.xdk7pt.x1xc55vz.x1emribx') #Try to find the pae
            index_chat = 0 
            for chat in self.notification:
                print(f'Trying to enter on the {index_chat}: {self.notification[index_chat]}')
                try:
                    chat.click()
                    print("Success to get the chat.")
                    sleep(2)
                    self.most_current_time = self.driver.find_elements(By.CSS_SELECTOR, 'span.x186z157.xk50ysn')
                    print(f'Most current time: {len(self.most_current_time)}')

                    self.itemClass = "html-div xe8uvvx xexx8yu x4uap5 x18d9i69 xkhd6sd x1gslohp x11i5rnm x12nagc x1mh8g0r x1yc453h x126k92a x18lvrbx".replace(' ','.') #Get all the messages of the chat.

                    if len(self.most_current_time) > 0:
                        for current_time in self.most_current_time:
                            self.string_current_time = current_time.text
                            print(f'Most recent chat: ' + self.string_current_time)
                            self.splited_string = self.string_current_time.split(':')
                            
                            self.chat_hour = int(self.splited_string[0])
                            self.chat_minutes = int(self.splited_string[1][0:1])

                            hour = datetime.now().hour
                            minute = datetime.now().minute

                            if hour >= self.chat_hour and minute >= self.chat_minutes:
                                print('itens encontrado: ')
                                self.all_content = self.driver.find_elements(By.CLASS_NAME, self.itemClass)
                                for message in self.all_content:
                                    if 'valor' in message.text:
                                        self.root_message = message.text
                                        print(f'User message: {self.root_message}')
                                        self.user_message_product = self.root_message
                                        break
                    else:
                        print('Cant find most recent chat, getting all messages...')
                        self.all_content = self.driver.find_element(By.CLASS_NAME, self.itemClass)
                        for message in self.all_content:
                            if 'valor' in message.text:
                                print(f'User message: {message.text}')
                                self.root_message = message.text
                                self.user_message_product = self.root_message
                                break
                except Exception as e:
                    print(e)
                    break
                index_chat += 1
        except Exception as e:
            print(e)

    def searchProduct(self, product):
        print(product)
        self.SEARCH_DRIVER = webdriver.Chrome()
        self.SEARCH_DRIVER.get('https://www.coocerqui.com.br/produtos/buscas?q='+product)

        input()

    def sendMessage(self):
        try:

            string_search = self.user_message_product
            index_valor = string_search.index('valor')
            new_string_search = string_search[index_valor:]
            splited_string_search = new_string_search.replace(' ', '%2B')
            self.searchProduct(splited_string_search)
            sleep(1)
            XPATH_TO_INPUT = '//p[contains(@class, "xat24cr") and contains(@class, "xdj266r")]'
            self.input_label = self.driver.find_element(By.XPATH, XPATH_TO_INPUT)
            self.input_label.send_keys(f'Hello! O produto: {self.root_message} esta saindo por R$ 10,00')
            sleep(0.5)
            try:
                self.input_label.send_keys(Keys.ENTER)
                sleep(2)
                print('Message sended...')
            except Exception as e:
                print('ERROR TO SEND MESSAGE: ' + e)
        except Exception as e:
            print(f'SEND MESSAGE ERROR\n\n{e}')

myInst = Instagram()
getNotifis = myInst.verifyNotifcatons()
print('GET NOTIFIS: ' + getNotifis)
if int(getNotifis)   > 0:
    msg = myInst.getMessage()
    if msg == False:
        print('Unable to send the message.')
    else:
        sendMessage = myInst.sendMessage()
        input()