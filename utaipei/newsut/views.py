from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import urllib.request
def home(request):
	wp1 = urllib.request.urlopen("http://www.utaipei.edu.tw/files/501-1000-1006-1.php?Lang=zh-tw")
	pw1 = wp1.read().decode('utf-8')
	wp1.close()
	soup1 = BeautifulSoup(pw1, 'html.parser')
	mylist1=soup1.find_all("span", class_="ptname ")
	wp2 = urllib.request.urlopen("http://www.utaipei.edu.tw/files/501-1000-1006-2.php?Lang=zh-tw")
	pw2 = wp2.read().decode('utf-8')
	wp2.close()
	soup2 = BeautifulSoup(pw2, 'html.parser')
	mylist2=soup2.find_all("span", class_="ptname ")
	mylist = mylist1+mylist2
	return render(request, "detail.html", {'mylist': mylist})

