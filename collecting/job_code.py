import requests
from bs4 import BeautifulSoup
import json
import re
import numpy as np

def upwork_job():
    # for i in range(1, 17):
    # c e_u_u_h: entire user url holder list
    e_u_u_h=[]
    for i in range(12, 13):
        # c u_u_h: user url holder list
        u_u_h = []
        url="https://smallbusinessexpo2018philadelphi.sched.com/directory/attendees/"+str(i)
        r=requests.get(url)
        c=r.content
        soup=BeautifulSoup(c, "html.parser")
        # videolist=soup.select('#sched-content-inner > div > div.sched-container-inner.sched-container-wide > div > div:nth-of-type(4) > a')
        # u_u_h.append("page"+str(i))
        for a in soup.find_all('a', {'class': 'sched-avatar'},href=True):
            u_u_h.append("https://smallbusinessexpo2018philadelphi.sched.com"+a["href"])
        e_u_u_h.append(u_u_h)
        # for i in len(videolist):
        #     print(i)
    # print("u_u_h",u_u_h)    
    # print("e_u_u_h",e_u_u_h)
    # thefile = open('test.txt', 'w')
    # for item in e_u_u_h:
    #     thefile.write("%s\n" % item)
    # c sq_e_u: squeezed entire url to (198,)
    sq_e_u=np.array(e_u_u_h).squeeze()

    # c e_u_d: entire user dictionary
    e_u_d={}
    # c e_u_d: entire user dictionary
    e_u_l=[]
    for i in sq_e_u:
        r=requests.get(str(i))
        c=r.content
        soup=BeautifulSoup(c, "html.parser")
        # print("soup",soup)

        # c one_p_n: one person name
        one_p_n=soup.find('h1', attrs={'id': "sched-page-me-name"}).text
        # print("one_p_n",one_p_n)
        e_u_l.append("Full name: "+str(one_p_n).replace("\n","").strip())

        # c one_p_c_p: one person company and position
        one_p_c_p=soup.find('div', {'id':'sched-page-me-profile-data'}).text
        e_u_l.append("Company and Position: "+str(one_p_c_p).replace("\n",""))

        # c one_p_nt: one person social network
        try:
            one_p_nt=soup.find('div', {'id':'sched-page-me-networks'}).text
            # print("one_p_nt",one_p_nt)
            e_u_l.append("Homepage: "+str(one_p_nt).replace("\n",""))
        except:
            # print("No social networks or homepage")
            pass
        
        print("e_u_l",e_u_l)    

upwork_job()
