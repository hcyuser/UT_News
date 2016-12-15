from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import urllib.request
def home(request):
	wp = urllib.request.urlopen("http://www.utaipei.edu.tw/files/501-1000-1006-1.php?Lang=zh-tw")
	pw = wp.read().decode('utf-8')
	soup = BeautifulSoup(pw, 'html.parser')
	mylist=soup.find_all("span", class_="ptname ")
	return render(request, "detail.html", {'mylist': mylist})

