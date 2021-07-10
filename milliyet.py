from typing import Text
import requests
from bs4 import BeautifulSoup
import time



url = "https://www.milliyet.com.tr/"
r = requests.get(url)
soup = BeautifulSoup(r.content,"lxml")
haberler = soup.find_all("div",attrs={"class":"main-card"})

print(len(haberler))
i=1


for haber in haberler:
    
    
    
    haber_link="https://www.milliyet.com.tr" + haber.a.get("href")
    haber_r=requests.get(haber_link)
    haber_soup=BeautifulSoup(haber_r.content,"lxml")
    
    haber_title=haber_soup.find_all("h3",attrs={"class":"main-card__head"})
    
    print(haber_title)
    
    haber_title1=haber.a.get("href")
   
    print(haber_title1)
    print("**************************")
    
    
    ayrintilar=haber_soup.find_all("div",attrs={"class":"gallery-group group_1"})
   
    #print(ayrintilar.prettify())
   
    #print(len(ayrintilar))  
    for ayrinti in ayrintilar:
        haber_text = ayrinti.find("h2",attrs={"class":"rhd-article-spot"})
        haber_text1 = ayrinti.find("h3",attrs={"class":"description"})
        print(haber_text)
        print(haber_text1)
        print("*************************************************")
        i+=1
        print(i)
        
       # if i == 8:
            #time.sleep(10)