#file 2

#Windows Based -pip install pyttsx3

import pyttsx3
def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[2].id)
    engine.setProperty('rate',170)
    # print(voices)
    print("")
    print(f"Wizard : {Text}")
    print("")
    engine.say(Text)
    engine.runAndWait()

# Crome Based -pip install selenium==4.1.3
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from time import sleep

# chrome_options = Options()
# chrome_options.add_argument('--log-level=3')
# chrome_options.headless = True
# Path = "DataBase\chromedriver.exe"
# driver = webdriver.Chrome(Path,options=chrome_options)
# driver.maximize_window()


# website =r"https://ttsmp3.com/text-to-speech/British%20English/"
# driver.get(website)
# ButtonSelection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
# ButtonSelection.select_by_visible_text('British English / Brian') #online voices selection

# def Speaka(Text):
#     lengthoftext = len(str(Text))

#     if lengthoftext==0:
#         pass

#     else:
#         print("")
#         print(f"Wizard: {Text}")
#         print("")
#         Data = str(Text)
#         xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
#         driver.find_element(By.XPATH,value=xpathofsec).send_keys(Data)
#         driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click()
#         driver.find_element(By.XPATH,value='/html/body/div[4]/div[2]/form/textarea').clear()

#         if lengthoftext>=30:
#             sleep(4)

#         if lengthoftext>=40:
#             sleep(6)

#         if lengthoftext>=55:
#             sleep(8)

#         if lengthoftext>=70:
#             sleep(10)

#         if lengthoftext>=100:
#             sleep(13)

#         if lengthoftext>=120:
#             sleep(14)

#         else:
#             sleep(2)



# Speak("Hello Sir, How Are You?")
# Speaka("Hello Sir, How Are You?")





