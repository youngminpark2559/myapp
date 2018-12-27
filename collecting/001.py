import requests
from bs4 import BeautifulSoup
import json
import re

def suggest():
    print("Page range you can select is between 1 and "+str(last_page_num))
    startpage=input('start page: ')
    lastpage=input('last page: ')
    return startpage,lastpage

def videolistwithtitle(startpage,lastpage):
    for i in list(range(int(startpage),int(lastpage)+1)):
        addressholder=[]
        url='https://channel9.msdn.com/Browse/AllContent?page='+str(i)+'&lang=en'
        r=requests.get(url)
        c=r.content
        soup=BeautifulSoup(c,"html.parser")
        # re = BeautifulSoup(r.text)

        videolist=soup.select('h3 > a[href]')
        print('\npage'+str(i))
        for onevideo in videolist:
            refinedaddress=str(onevideo).replace('<a href="','https://channel9.msdn.com/')\
                                        .replace('">',  '\nabove video\'s title : ')\
                                        .replace('</a>','')
            print(refinedaddress)

def videolistwithouttitle(startpage,lastpage):
    for i in list(range(int(startpage),int(lastpage)+1)):
        addressholder=[]
        url='https://channel9.msdn.com/Browse/AllContent?page='+str(i)+'&lang=en'
        r=requests.get(url)
        c=r.content
        soup=BeautifulSoup(c,"html.parser")
        # re = BeautifulSoup(r.text)

        videolist=soup.select('h3 > a[href]')
        print('\npage'+str(i))

        listHolder=[]

        for onevideo in videolist:
            refinedaddress=str(onevideo).replace('<a href="','https://channel9.msdn.com/')\
                                        .replace('">','\nabove video\'s title : ')\
                                        .replace('</a>','')
            listremovedtitle=re.sub(r'(above video).*','',refinedaddress)
            print(listremovedtitle)

def videolistwithMp3list(startpage,lastpage):
    for i in list(range(int(startpage),int(lastpage)+1)):
        addressholder=[]
        url='https://channel9.msdn.com/Browse/AllContent?page='+str(i)+'&lang=en'
        r=requests.get(url)
        c=r.content
        soup=BeautifulSoup(c,"html.parser")
        # re = BeautifulSoup(r.text)

        videolist=soup.select('h3 > a[href]')
        print('\npage'+str(i))

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

if __name__ == '__main__':
    url='https://channel9.msdn.com/Browse/AllContent'
    r=requests.get(url)
    c=r.content
    soup=BeautifulSoup(c,"html.parser")

    last_page_num=soup.select('body > main > div.paging.nav.holder > div > ul > li:nth-of-type(5) > a')
    last_page_num_str=''.join(map(str,last_page_num))
    last_page_num=last_page_num_str.replace("\t","")\
                                   .replace("\n","")\
                                   .replace("\r","")\
                                   .split(">")[-2].replace("</a","")

    titleNonTitleMp3=int(input('video list+title(1), video list(2), video list+mp3 list(3): '))
    if titleNonTitleMp3==1:
        startpage,lastpage=suggest()
        videolistwithtitle(startpage,lastpage)
    elif titleNonTitleMp3==2:
        startpage,lastpage=suggest()
        videolistwithouttitle(startpage,lastpage)
    elif titleNonTitleMp3==3:
        startpage,lastpage=suggest()
        videolistwithMp3list(startpage,lastpage)

# Option 1 result
# page1
# https://channel9.msdn.com//Blogs/One-Dev-Minute/One-Dev-Question-Is-VSCode-a-Microsoft-product-and-does-it-only-run-on-Windows
# above video's title : One Dev Question - Is VSCode a Microsoft product and does it only run on Windows?
# https://channel9.msdn.com//Blogs/One-Dev-Minute/One-Dev-Question-Can-you-use-Git-in-VSCode
# above video's title : One Dev Question - Can you use Git in VSCode?
# ...

# Option 2 result
# page1
# https://channel9.msdn.com//Shows/Blocktalk/Writing-Dapps-with-Drizzle
# https://channel9.msdn.com//Shows/Blocktalk/Develop-locally-with-Ganache
# ...

# Option 3 result
# page1
# wget https://sec.ch9.ms/ch9/e6b3/359a7596-d363-4c66-a705-3f674896e6b3/MicrosoftProduct.mp3 &&
# wget https://sec.ch9.ms/ch9/9e1b/d00dd4b1-1285-47e0-bd91-e77490399e1b/GitVSCode.mp3 &&
# ...
