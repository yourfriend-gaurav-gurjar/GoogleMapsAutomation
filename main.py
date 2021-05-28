from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import os
pin=""
os.system('cls')
os.system('color 0a')
#Inputs
destination=input("Where do you want to go ? ")
addrs=input("Enter your Colony,House Name,etc. : ")
pin=input("Enter your ZIP-CODE : ")
#MainLoop
if pin !="":
    path="chromedriver.exe"
    driver = webdriver.Chrome(path)
    #password=input("Enter your password : ")
    driver.get("https://www.google.com/maps/")
    os.system('cls')
    print("Recieving info Please Wait !")
    def lookfor(location):
        WebDriverWait(driver,100).until(presence_of_element_located((By.XPATH,"/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div/div[3]/div/input[1]"))).send_keys(location)
        WebDriverWait(driver,100).until(presence_of_element_located((By.XPATH,"/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button"))).click()
    def get_directions(home,location):
        lookfor(location)
        WebDriverWait(driver,100).until(presence_of_element_located((By.XPATH,"//*[@id='pane']/div/div[1]/div/div/div[4]/div[1]/div/button"))).click()
        WebDriverWait(driver,100).until(presence_of_element_located((By.XPATH,"/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input"))).send_keys(pin+" "+addrs)
        WebDriverWait(driver,100).until(presence_of_element_located((By.XPATH,"/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]"))).click()
        #Car Data
        WebDriverWait(driver,100).until(presence_of_element_located((By.XPATH,"/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/button"))).click()
        distance=WebDriverWait(driver,100).until(presence_of_element_located((By.XPATH,"/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[8]/div[1]/div/div[1]/div[1]/div[2]/div"))).get_attribute('innerHTML').strip()
        l=len("The distance from {} to {} is {}s".format(home,location,distance))
        for i in range(0,l):
            print("-",end='')
        print()
        print("The distance from {} to {} is {}s".format(home,location,distance))
        for i in range(0,l):
            print("-",end='')
        print()
        car_time=WebDriverWait(driver,100).until(presence_of_element_located((By.XPATH,"/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[8]/div[1]/div/div[1]/div[1]/div[1]/span[1]"))).get_attribute('innerHTML').strip()
        car_route=WebDriverWait(driver,100).until(presence_of_element_located((By.XPATH,"/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[8]/div[1]/div/div[1]/div[2]/h1[1]/span"))).get_attribute('innerHTML').strip()
        l=len("The fastest Car route is {} long and its via {}".format(car_time,car_route))
        for i in range(0,l):
            print("-",end='')
        print()
        print("<=FASTEST CAR ROUTE =>")
        print()
        print("TIME : {}\nROUTE : {}\n".format(car_time,car_route))
        print("The fastest Car route is {} long and its via {}".format(car_time,car_route))
        for i in range(0,l):
            print("-",end='')
        print()
        print()
        #Train Data
        WebDriverWait(driver,100).until(presence_of_element_located((By.XPATH,"/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div[3]/button"))).click()
        train_time=WebDriverWait(driver,100).until(presence_of_element_located((By.XPATH,"/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[8]/div/div/div[2]/div[1]/div"))).get_attribute('innerHTML').strip()
        train_arrival=WebDriverWait(driver,100).until(presence_of_element_located((By.XPATH,"/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[8]/div/div/div[2]/div[3]/div/span[1]/span[1]"))).get_attribute('innerHTML').strip()
        train_station=WebDriverWait(driver,100).until(presence_of_element_located((By.XPATH,"/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[8]/div/div/div[2]/div[3]/div/span[1]/span[2]"))).get_attribute('innerHTML').strip()
        train_name=WebDriverWait(driver,100).until(presence_of_element_located((By.XPATH,"/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[8]/div/div/div[2]/div[2]/span/span[2]/span[1]/span[1]/span"))).get_attribute('innerHTML').strip()
        l=len("Fastest Train journey will be {} long TRAIN NAME : {} The train will leave at {} from {}".format(train_time,train_name,train_arrival,train_station))
        for i in range(0,l):
            print("-",end='')
        print()
        print("<= FASTEST TRAIN ROUTE =>")
        print()
        print("TIME : {}\nTRAIN NAME : {}\nTRAIN DEPT TIME : {}\nSTATION : {}\n".format(train_time,train_name,train_arrival,train_station))
        print("Fastest Train journey will be {} long TRAIN NAME : {} The train will leave at {} from {}".format(train_time,train_name,train_arrival,train_station))
        for i in range(0,l):
            print("-",end='')
        print()
    get_directions(addrs,destination)
    x=input()
