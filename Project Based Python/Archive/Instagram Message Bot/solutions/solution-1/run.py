# Source Code Link:
# https://data-flair.training/blogs/python-instagram-bot-automate-messages/

# Import libraries
from selenium import webdriver
import time
import random
import requests
from bs4 import BeautifulSoup
#-------------------------------------------------------------------------------------#
def jokes():
    #Open the website to scrape the jokes from
    result = requests.get('https://bestlifeonline.com/one-liner-jokes/')
    #Html parser using beautiful soup
    soup = BeautifulSoup(result.content, 'html.parser')
    #print(result.status_code)
    #Choose a random joke
    joke_number = random.randint(1,20)
    #Using the HTML parser, find the ordered list tag and then the list item tags
    #Extract the random joke
    joke = soup.ol.find_all("li")[joke_number]
    #print(len(joke))
    #Return only the text ie joke and not the entire tag
    return joke.text
#-------------------------------------------------------------------------------------#

def login_to_instagram():
    #Find username
    Username=browser.find_element_by_name("username")
    #Send username details
    Username.send_keys("enter username")
    #Find password
    password=browser.find_element_by_name("password")
    #Send password details
    password.send_keys("enter password")
    #Submit button
    browser.find_element_by_xpath("//button[@type='submit']").click()
#-------------------------------------------------------------------------------------#

def skip_buttons():
    #Not now button for not saving the password
    browser.find_element_by_xpath("//div[@class='cmbtv']/button[@type='button']").click()
    #Turn off the notifications button
    browser.find_element_by_xpath("//div[@class='mt3GC']/button[@class='aOOlW   HoLwm ']").click()
#-------------------------------------------------------------------------------------#

def navigate_to_sender():
    #Find the messages button
    browser.find_element_by_css_selector('html.js.logged-in.client-root.js-focus-visible.sDN5V body div#react-root section._9eogI.E3X2T nav.NXc7H.jLuN9 div._8MQSO.Cx7Bp div._lz6s div.MWDvN div.ctQZg div._47KiJ div.XrOey a.xWeGp svg._8-yf5').click()
    #Find the chat of the intended person
    elements = browser.find_elements_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div')
    length = len(elements)   
    for i in range(length):
        find_user = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[{}]/a/div/div[2]/div[1]/div/div/div/div'.format(str(i+1)))
        if find_user.text == username:
            find_user.click()
#-------------------------------------------------------------------------------------# 

def send_jokes(time_between_jokes):
    #Find the text area in the chat to send message
    message_entry=browser.find_element_by_css_selector('html.js.logged-in.client-root.js-focus-visible.sDN5V body div#react-root section._9eogI.DT7qQ div.t30g8.L1C6I div.Igw0E.IwRSH.eGOV_._4EzTm div.oYYFH div.pV7Qt._6Rvw2.Igw0E.IwRSH.YBx95.ybXk5._4EzTm.i0EQd div.DPiy6.Igw0E.IwRSH.eGOV_.vwCYk div.uueGX div.JiVIq._0NM_B div.Igw0E.IwRSH.eGOV_._4EzTm div.Igw0E.IwRSH.eGOV_._4EzTm.L-sTb.HcJZg div.X3a-9 div.Igw0E.IwRSH.eGOV_.vwCYk.ItkAi textarea')
    while True:
        #Call jokes function to get a random joke
        joke = jokes()
        #Send the joke to the text box
        message_entry.send_keys('Howdy Partner!!!! '+joke+ ' Joke was sent on {time}'.format(time=time.ctime()))
        #Click on the send buttons
        browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
        #Send another joke after the timeout
        time.sleep(time_between_jokes)
#-------------------------------------------------------------------------------------#

#Read user input to set a delay between jokes and obtain the username
time_between_jokes = int(input("Enter the seconds of delay between each joke: "))
username = input("Enter username: ")

#Open the webbrowser and use it for autonomous control
browser = webdriver.Firefox(executable_path='/home/deepika/Downloads/internship/instagram/geckodriver')
#Open the URL in the opened webbrowser
browser.get('https://instagram.com/')
#Start using the functions after a delay
browser.implicitly_wait(5)
#Call all the functions in order based on webpages
login_to_instagram()
skip_buttons()
navigate_to_sender()
send_jokes(time_between_jokes)