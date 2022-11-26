def getsociallinks():
    list = soup.find(class_="flex my-2 -mx-1 justify-center")
    sociallinks = [links.get('href') for links in list]
    return sociallinks

def getemail():
    elist = soup.find('a')
    mail_list = [links.get('href="mailto:\w"') for links in elist]
    return mail_list

def getcontact():
    clist = soup.find(class_="text-base leading-4 text-white cursor-pointer flex items-center justify-center md:justify-start mb-4r")
    contact = [links.get('href') for links in clist]
    return contact

import requests
from bs4 import BeautifulSoup

req = requests.get('https://ful.io')
soup = BeautifulSoup(req.content,"html.parser")


print("Social Links-")
sp = getsociallinks()
print(sp[0]+"\n"+sp[1]+"\n\n")












# print()



