
import requests
from bs4 import BeautifulSoup
url =  "https://www.python.org/jobs/"
r = requests.get(url) 
soup = BeautifulSoup(r.content,"lxml")
pages = len(soup.find_all("ul",attrs={"class":"pagination menu"})[0].find_all("li"))-2
totalJobs=0

for pageNumber in range(1,pages+1):
    pageRequest = requests.get("https://www.python.org/jobs/?page=" + str(pageNumber))
    pageSource = BeautifulSoup(pageRequest.content,"lxml")
    jobs = pageSource.find("div",attrs={"class":"row"}).ol.find_all("li")
    #TÜM İŞLERİ ÇEKTİK DÖNGÜ İLRE İLAN DETAYLARINI ALALIM
    for job in jobs:
        name=job.h2.find("a").text
        location =job.find("span",attrs={"class":"listing-location"}).text
        company=job.find("span",attrs={"class":"listing-company-name"}).br.next.strip
        #publishtime=jobs.find("time").text
   
        print(name,company,location,sep="\n")
        print("_"*60)
       
       