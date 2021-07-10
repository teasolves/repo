from typing import Text
import requests
from bs4 import BeautifulSoup



url = "https://www.milliyet.com.tr/"
r = requests.get(url)
soup = BeautifulSoup(r.content,"lxml")
haberler = soup.find_all("div",attrs={"class":"main-card"})

#print(haberler)


for haber in haberler:
    haber_link="https://www.milliyet.com.tr" + haber.a.get("href")
    haber_r=requests.get(haber_link)
    haber_soup=BeautifulSoup(haber_r.content,"lxml")
   
    #print(haber_soup.prettify())
    
    
    ayrintilar=haber_soup.find_all("div",attrs={"class":"gallery-group group_1"})
   
    #print(ayrintilar.prettify())
    
     
    for ayrinti in ayrintilar:
        haber_text = ayrinti.find("h2",attrs={"class":"rhd-article-spot"})
        haber_text1 = ayrinti.find("h3",attrs={"class":"description"})
        print(haber_text)
        print(haber_text1)