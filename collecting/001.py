import requests
from bs4 import BeautifulSoup
import json
import re
import numpy as np

def suggest():
  startpage=input('start page: ')
  lastpage=input('last page: ')
  return startpage,lastpage

def use_random_pages(how_many_pages):
  np.random.seed(0)

  # c rand_nums: random numbers
  random_num_li=np.random.randint(1,last_page,size=how_many_pages)

  return random_num_li

def videolistwithtitle(nums_list):
  for i in nums_list:
    addressholder=[]
    url='https://channel9.msdn.com/Browse/AllContent?page='+str(i)+'&lang=en'
    r=requests.get(url)
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    # re = BeautifulSoup(r.text)

    videolist=soup.select('h3 > a[href]')
    print('\npage: '+str(i))
    for onevideo in videolist:
      refinedaddress=str(onevideo).replace('<a href="','https://channel9.msdn.com/')\
                                  .replace('">',  '\nabove video\'s title : ')\
                                  .replace('</a>','')
      print(refinedaddress)

def videolistwithouttitle(nums_list):
  for i in nums_list:
    addressholder=[]
    url='https://channel9.msdn.com/Browse/AllContent?page='+str(i)+'&lang=en'
    r=requests.get(url)
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    # re = BeautifulSoup(r.text)

    videolist=soup.select('h3 > a[href]')
    print('\npage: '+str(i))

    listHolder=[]

    for onevideo in videolist:
      refinedaddress=str(onevideo).replace('<a href="','https://channel9.msdn.com/')\
                                  .replace('">','\nabove video\'s title : ')\
                                  .replace('</a>','')
      listremovedtitle=re.sub(r'(above video).*','',refinedaddress)
      print(listremovedtitle)

def videolistwithMp3list(nums_list):
  for i in nums_list:
    addressholder=[]
    url='https://channel9.msdn.com/Browse/AllContent?page='+str(i)+'&lang=en'
    r=requests.get(url)
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    # re = BeautifulSoup(r.text)

    videolist=soup.select('h3 > a[href]')
    print('\npage: '+str(i))

    for onevideo in videolist:
      refinedaddress=str(onevideo).replace('<a href="','https://channel9.msdn.com/')\
                                  .replace('">','\nabove video\'s title : ')\
                                  .replace('</a>','')
      listremovedtitle=re.sub(r'(above video).*','',refinedaddress).strip()
      # print(listremovedtitle)
      
      refinedaddressPage=requests.get(listremovedtitle)
      refinedaddressPageContents=refinedaddressPage.content
      soupForrefinedaddressPageContents=BeautifulSoup(refinedaddressPageContents,"html.parser")
      
      # This area is where I find mp3 address by index
      # mediaList=soupForrefinedaddressPageContents.find_all("div",{"class":"download"})
      # for media in mediaList:
      #     mp3Address=media.select('li > a[href]')
      #     splitedByHref=str(mp3Address[0]).split('href')
      #     oneMp3=str(splitedByHref).strip().split('>')[0].split('\'="')[1].replace('mp3"','mp3')
      #     print(oneMp3)

      # This area is where I find mp3 address by regular expression
      mediaList=soupForrefinedaddressPageContents.find_all("div",{"class":"download"})
      for media in mediaList:
        mediaAddress=str(media.select('li > a[href]'))
        try:
          extractedMp3=re.match('.*(mp3)',mediaAddress).group(0)
          print("wget "+str(extractedMp3).split('href="')[1]+" &&")
        except:
          pass

if __name__=='__main__':
  url='https://channel9.msdn.com/Browse/AllContent'
  r=requests.get(url)
  c=r.content
  soup=BeautifulSoup(c,"html.parser")

  url='https://channel9.msdn.com/Browse/AllContent?&lang=en'
  r=requests.get(url)
  c=r.content
  soup=BeautifulSoup(c,"html.parser")
  # re = BeautifulSoup(r.text)

  videolist=soup.select('body > main > div.paging.nav.holder > div > ul > li:nth-of-type(5) > a')
  last_page_num=int(str(videolist[0]).replace("\t","").replace("\r\n","").split(">")[-2].split("<")[0])
  print("The page range you can select is between 1 and "+str(last_page_num))

  # c random_range: which one will you use from random pages and range pages
  random_range=int(input('random pages(1), range pages(2): '))
  print("")
  if random_range==1:
    how_many_pages=int(input('how many pages do you want: '))
    print("")
    random_num_li=use_random_pages(how_many_pages)
    videolistwithMp3list(random_num_li)
  else:
    titleNonTitleMp3=int(input('video list+title(1), video list(2), video list+mp3 list(3): '))
    print("")
    startpage,lastpage=suggest()
    s_l_li=startpage,lastpage
    nums_list=list(range(int(s_l_li[0]),int(s_l_li[1])+1))
    if titleNonTitleMp3==1:
      videolistwithtitle(nums_list)
    elif titleNonTitleMp3==2:
      videolistwithouttitle(nums_list)
    elif titleNonTitleMp3==3:
      videolistwithMp3list(nums_list)

# ======================================================================
# Example from random pages
# page1654
# wget https://sec.ch9.ms/ch9/55e8/9fdb1353-c1eb-45a5-b38b-f0f966da55e8/aspnet26509.mp3 &&
# wget https://sec.ch9.ms/ch9/fabb/275fcd03-5bac-435b-bd34-c7fd353afabb/aspnet26508.mp3 &&
# wget https://sec.ch9.ms/ecn/ch9/4/8/0/8/9/4/podcast9017.mp3 &&
# page836
# wget https://sec.ch9.ms/ch9/caa6/db6e189f-5671-4a05-a10d-7373961ccaa6/SharingInvitation.mp3 &&
# wget https://sec.ch9.ms/ch9/deb0/e2fe8bd3-e94c-4e55-9dc1-b4b08c5ddeb0/SearchFilesFolders.mp3 &&
# wget https://sec.ch9.ms/ch9/92de/21b1cf8b-b842-43eb-a43a-c4fbf15a92de/SettingsforOneDrive.mp3 &&
# wget https://sec.ch9.ms/ch9/81e2/1884fde6-a944-46cc-9e82-d99bd39f81e2/PicHitme.mp3 &&
# wget https://sec.ch9.ms/ch9/7535/806c3ce1-a421-4779-a0d2-e7fdea4f7535/youthsparkwebinar.mp3 &&
# wget https://sec.ch9.ms/ch9/9ba1/8566da5f-d7cb-4da5-a657-dac722df9ba1/emailprivacywebinar.mp3 &&
# wget https://sec.ch9.ms/ch9/a365/1c1177dc-f751-4623-a091-d831e46ea365/AzureRemoteAppAsktheExpertsWebinarOne.mp3 &&
# wget https://sec.ch9.ms/ch9/0b1a/5ada9936-896b-43fc-a3df-4189f3a80b1a/DefragTools123.mp3 &&
# wget https://sec.ch9.ms/ch9/8ef0/42ac15de-409c-463e-9db7-e57e5cdc8ef0/ChainBridgeTech.mp3 &&
# wget https://sec.ch9.ms/ch9/e899/d25b0ad0-2585-42a2-bb86-66b6ad59e899/ChangeWinAppLocation.mp3 &&

# ======================================================================
# Example from range pages
# Option 1 result
# The page range you can select is between 1 and 2455
# random pages(1), range pages(2): 
# video list+title(1), video list(2), video list+mp3 list(3): 
# start page: last page: page: 1
# https://channel9.msdn.com//Blogs/One-Dev-Minute/One-Dev-Question-with-Larry-Osterman-What-is-DCOM-about
# above video's title : One Dev Question with Larry Osterman - What is DCOM about?
# https://channel9.msdn.com//Shows/This+Week+On+Channel+9/TWC9-Visual-Studio-2019-Nodejs-and-Cosmos-DB-GitHub-Draft-Pull-Requests-and-more
# page: 2
# https://channel9.msdn.com//Blogs/One-Dev-Minute/One-Dev-Question-with-Raymond-Chen-What-was-your-first-project-at-Microsoft
# above video's title : One Dev Question with Raymond Chen - What was your first project at Microsoft?
# https://channel9.msdn.com//Shows/Azure-Friday/Azure-Instance-Metadata-Service-updates-for-attested-data
# page: 3
# https://channel9.msdn.com//Shows/Internet-of-Things-Show/Azure-IoT-Edge-VM-on-Azure-Marketplace
# above video's title : Azure IoT Edge VM on Azure Marketplace
# https://channel9.msdn.com//Shows/Blocktalk/Ethereum-Name-Service

# --------------------------------------------------
# Option 2 result
# The page range you can select is between 1 and 2455
# random pages(1), range pages(2): 
# video list+title(1), video list(2), video list+mp3 list(3): 
# start page: last page: page1
# https://channel9.msdn.com//Blogs/One-Dev-Minute/One-Dev-Question-with-Larry-Osterman-What-is-DCOM-about

# https://channel9.msdn.com//Shows/This+Week+On+Channel+9/TWC9-Visual-Studio-2019-Nodejs-and-Cosmos-DB-GitHub-Draft-Pull-Requests-and-more

# page2
# https://channel9.msdn.com//Blogs/One-Dev-Minute/One-Dev-Question-with-Raymond-Chen-What-was-your-first-project-at-Microsoft

# https://channel9.msdn.com//Shows/Azure-Friday/Azure-Instance-Metadata-Service-updates-for-attested-data

# page3
# https://channel9.msdn.com//Shows/Internet-of-Things-Show/Azure-IoT-Edge-VM-on-Azure-Marketplace

# https://channel9.msdn.com//Shows/Blocktalk/Ethereum-Name-Service

# --------------------------------------------------
# Option 3 result
# The page range you can select is between 1 and 2455
# random pages(1), range pages(2): 
# video list+title(1), video list(2), video list+mp3 list(3): 
# start page: last page: page1
# wget https://sec.ch9.ms/ch9/e41b/7f81b468-4164-43ff-a319-732a6f9de41b/DCOM.mp3 &&
# wget https://sec.ch9.ms/ch9/cca0/e5526952-9693-45a8-94cb-ae6d00adcca0/TWC9.mp3 &&
# page2
# wget https://sec.ch9.ms/ch9/292f/073001be-caa1-4bb3-9d19-47d14d76292f/FirstProject.mp3 &&
# wget https://sec.ch9.ms/ch9/b640/10494b42-836c-463c-804c-b2fbf88bb640/AzFrInstanceMetadataUpdates.mp3 &&
# page3
# wget https://sec.ch9.ms/ch9/032b/47e940ef-3296-4cfa-853d-aa44c980032b/IoTShow3.mp3 &&
# wget https://sec.ch9.ms/ch9/279e/5351f657-6e28-4271-ad28-acf19b44279e/ethereumnameservice.mp3 &&
