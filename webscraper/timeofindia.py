from bs4 import BeautifulSoup
import subprocess
import requests
import time

url = "https://timesofindia.indiatimes.com/"

def open_url(url):
    return requests.get(url).text  # returns html

def get_bsoup_object(html):
    return BeautifulSoup(html, "lxml")  # returns soup (BeautifulSoup's object)


def sendmessage(message):
    subprocess.Popen(['notepad.exe', message])
    return


def main():
	myhtml = open_url(url)
	soup = get_bsoup_object(myhtml)
	j = 1
	
	for i in soup.find('ul',attrs={'class':'list9'}).findAll('li'):
		#print(str(j) + " " + i.text)
		sendmessage(str(j) + " " + i.text)
		time.sleep(10)
		j += 1
		


while True:
	main()
	time.sleep(36000)