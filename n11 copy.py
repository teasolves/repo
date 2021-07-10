from typing import Text
import requests
from bs4 import BeautifulSoup

for sayfaNo in range (1,3):

    url= "https://www.n11.com/telefon-ve-aksesuarlari/cep-telefonu?page"+str(sayfaNo)
    r = requests.get(url)
    soup = BeautifulSoup(r.content,"lxml")
    urunler = soup.find_all("li",attrs={"class":"column"})
   


    for urun in urunler:
        urunAdi=(urun.a.get("title"))
        urunLink=(urun.a.get("href"))
        #print(urunAdi ,"****************************************")
        
        urun_r = requests.get(urunLink)
        urun_soup=BeautifulSoup(urun_r.content,"lxml")
        ozellikler=urun_soup.find_all("ul", attrs={"class":"unf-prop-list"})
        #print(ozellikler)
        

        for ozellik in ozellikler:
            
            deneme=ozellik.find("li", attrs={"class":"unf-prop-list-item"})
            
            #test = ozellik.find("li", attrs={"class":"unf-prop-list-prop"}).find("p").text
            
            print(deneme.text)
            
            #print(test)
            #print(deneme.find_all("p", attrs={"class":"unf-prop-list-title"}))
            #print(deneme.find("p", attrs={"class":"unf-prop-list-prop"}))