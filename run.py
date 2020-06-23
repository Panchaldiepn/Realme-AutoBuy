import os
from pathlib import Path
import re
import sys
from __banner.banner import banner
import pause
from datetime import datetime

######### AUTHOR - @AmmeySaini #########
######### Github Repo -  https://github.com/AmmeySaini/Realme-AutoBuy #########
######### I'm not responisble for any damage or anything bad happens to you using this script #########
######### Use it on your own RISK #########
######### This is only for educational purpose #########

def main():

	sys.stdout.write(banner())

	product_id1 = input('Enter product id or Sale url: ')
	if '/in/goods/' in product_id1 or product_id1.isdigit():
		product_id = re.findall(r'\d+', product_id1)[0]
	else:
		print('\nIncorrect Sale url\nSale Url should be like https://buy.realme.com/in/goods/188')
		exit()
	all_cookies = input('Enter cookie file(s) on which you want to order seprated with comma "," ex- cookie1.txt,cookie2.txt ')

	cookie_list = []

	regex = re.compile(',')
	if(regex.search(all_cookies) != None):
		c_ar = all_cookies.split(',')
		for c in c_ar:
			c = c.strip()
			cookie_file = Path('./my_cookies/' + c)
			if cookie_file.exists():
				cookie_list.append(c)
				added = 1
			else:
				added = 0
				print('\nSeems like your cookie file (' + c + ') doesn\'t exists in my_cookies folder\nPlease add all your cookie files to my_cookies folder')
				exit()
	else:
		cook = all_cookies.strip()
		cookie_file = Path('./my_cookies/' + cook)
		if cookie_file.exists():
			cookie_list.append(cook)
			added = 1
		else:
			added = 0
			print('\nSeems like your cookie file (' + cook + ') doesn\'t exists in my_cookies folder\nPlease add all your cookie files to my_cookies folder')
			exit()
	if added == 1:
		print('Cookie files added')
		s_year = input('Year as YYYY: ')
		s_month = input('Month as M: ')
		s_date = input('Date as D: ')
		s_hour = input('Hour as H: ')
		s_minute = input('Minute as M: ')	
		pause.until(datetime(int(s_year), int(s_month), int(s_date), int(s_hour), int(s_minute), 0))
		print('\nNext step will be proceed at your provided time. Wait till then... ')
		for i in cookie_list:
			os.system('start cmd /k python realme.py -c ' + i + ' -id ' + str(product_id))

if __name__ == '__main__':
	main()
