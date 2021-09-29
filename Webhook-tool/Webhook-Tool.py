import colorama
import requests
import time
import json
import sys
from time import sleep
from colorama import Fore, Back, Style
from os import system
from colorama import init
from os import system
import sys
from art import *
import os
import json
import os
import time
from time import sleep
#Software made by BAD#8938
#The owner of this software is not responsible of the activity the software can procure
#Don't resell this software at your own purpose



system("title " + "Webhook Tool - By BAD#8938")
os.system('mode con: cols=1920 lines=1080')





def spam():
    system("title " + "Webhook Tool - Spamming webhook")
    n = 0
    webhookURL = input(Fore.MAGENTA + "\nInput webhook URL:\n")
    message = input(Fore.MAGENTA +"Input message to send:\n")
    username = input(Fore.MAGENTA +"Input bot username:\n")
    amount = int(input(Fore.MAGENTA +"Input amount of messages:\n"))
    
    payload = {
      'content': message,
      'username': username,
    }

    for i in range(amount):
        req = requests.post(webhookURL, data=payload)
        n +=1
        print(Fore.GREEN,n,"|",amount, " Succes")
        time.sleep(0.2) # sleep so it doesnt timeout
    system('cls')
    menu()

def delete():
    system("title " + "Webhook Tool - Deleting Webhook")
    webhookURL = input(Fore.GREEN +"\nInput webhook URL:\n")
    system("title " + "Webhook Tool - Deleting Webhook.")
    time.sleep(0.5)
    system("title " + "Webhook Tool - Deleting Webhook..")
    time.sleep(0.5)
    system("title " + "Webhook Tool - Deleting Webhook...")
    time.sleep(0.5)
    system("title " + "Webhook Tool - Deleting Webhook.")
    time.sleep(0.5)
    system("title " + "Webhook Tool - Deleting Webhook..")
    time.sleep(0.5)
    system("title " + "Webhook Tool - Deleting Webhook...")
    payload = {
    'content': 'Your Webhook as been deleted. Have a good day!',
    'username': 'Deleted',
    }
    try:
        requests.post(webhookURL, data=payload)
        requests.delete(webhookURL)
        print(Fore.RED +"Webhook = Deleted")
    except:
        print(Fore.RED +"Webhook url doesn't exist")
        time.sleep(3)
        system('cls')
    system('cls')
    menu()
    
def info():
    system("title " + "Webhook Tool - Information menu")
    webhookURL = input(Fore.GREEN +"\nInput webhook URL:\n")
    try:
        req = requests.get(webhookURL)
        y = json.loads(req.content)
    
        print("\nName:",y['name'])
        print("token:",y['token'])
        print("id:",y['id'])
        print("channel id:",y['channel_id'])
        print("guild id:",y['guild_id'])
        menu()
    except:
        print(Fore.RED +"Webhook url doesn't exist")
        time.sleep(2)
        system('cls')
        menu()

        
def menu():
    tprint("Webhook Tool", font="starwars")
    system("title " + "Webhook Tool - By BAD#8938")
    print (Fore.MAGENTA +"\n<1> - Webhook Spammer\n")
    print (Fore.MAGENTA +"<2> - Webhook Deleter\n")
    print (Fore.MAGENTA +"<3> - Webhook Info\n")
    print (Fore.MAGENTA +"<4> - Webhook Publictity\n")
    r = input(Fore.GREEN +"Select an option <1-3>: ")
    
    if r == '1':
        spam()
    elif r == '2':
        delete()
    elif r == '3':
        info()
    elif r == '4':
        pub()
    else:
        print(Fore.RED +"\nChoice between 1-3")
        time.sleep(1)
        menu()
def pub(): 
    system("title " + "Webhook Tool - Publicity Menu")
    url = input(Fore.MAGENTA + "\nInput webhook URL:\n")
    message = input(Fore.MAGENTA +"Input Publicity to send:\n")
    username = input(Fore.MAGENTA +"Input bot username:\n")
    title = input(Fore.MAGENTA +"Input Publicity name\n")
    amount = int(input(Fore.MAGENTA +"Input amount of Publicity:\n"))





    data = {
        "content" : "",
        "username" : username
    }
    data["embeds"] = [
        {
            "description" : message,
            "title" : title
        }
    ]
    result = requests.post(url, json = data)
    n=0
    try:
        for i in range(amount):
            n+=1
            result = requests.post(url,json=data)
            print(Fore.GREEN +"Webhook =",n,"|",amount," as been sent")
    except:
        for i in range(amount):
            n-=1
            print(Fore.RED +"Webhook =",n,"|",amount," Failed")
menu()