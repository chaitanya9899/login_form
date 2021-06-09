import pandas as pd
import numpy as np

import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

Date_lst=[]
CourseName_lst=[]
RC_meetingItem_time=[]
RC_meetingItem_name=[]

driver=webdriver.Chrome(ChromeDriverManager().install())
def DataExtractRacingpost(url):

    driver.get(url)

    sleep(3)
    page_source = driver.page_source
    soup1 = BeautifulSoup(page_source, 'lxml')
    type(soup1)
    bs4.BeautifulSoup
    title = soup1.title
    
    
    CourseHeaderName_tag=soup1.find_all("div",{"class":"RC-accordion__courseInfo"})
    
    #section_tags=soup1.find_all("section")
    
    RC_meetingList_tag=soup1.find_all("div",{"class":"RC-meetingList"})
    
    for i in range(0,len(CourseHeaderName_tag)):
        
        HeaderName=CourseHeaderName_tag[i].text.replace("\n","").replace(" ","")
        
        print(HeaderName)
        
        #Div Race meeting list
        
        
        RC_meetingItem_tag=RC_meetingList_tag[i].find_all("div",{"class":"RC-meetingItem"})
        
        len(RC_meetingItem_tag)
        for j in range(0,len(RC_meetingItem_tag)):
            
            
            #Race meeting time
            RC_meetitem_time_tag=RC_meetingItem_tag[j].find("span",{"class":"RC-meetingItem__timeLabel"})
            RC_meetitem_time=RC_meetitem_time_tag.text.replace("\n","").replace(" ","")
            RC_meetingItem_time.append(RC_meetitem_time)
            #Race meeting Item
            RC_meetitem_Name_tag=RC_meetingItem_tag[j].find("div",{"class":"RC-meetingItem__section"})
            RC_meetitem_Name=RC_meetitem_Name_tag.text.replace("\n","").replace(" ","")
            RC_meetingItem_name.append(RC_meetitem_Name)
        
            CourseName_lst.append(HeaderName)

    
    
    print(RC_meetingItem_time) 
    print(RC_meetingItem_name) 
    print(CourseName_lst)

DataExtractRacingpost("https://www.racingpost.com/racecards/2020-12-02/")

def DataToExcel():
    df = pd.DataFrame(data={"Header Name":CourseName_lst,"Race Time":RC_meetingItem_time,"Name":RC_meetingItem_name})
    writer = pd.ExcelWriter(r"Racingpost(today).xlsx", engine='xlsxwriter')
    
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    #df..to_excel(r"D:\CollegeDunia\DataBase\IndiaveterinaryCollegeURLS.csv", sep=',',index=False)
    df.head(50)



DataToExcel()