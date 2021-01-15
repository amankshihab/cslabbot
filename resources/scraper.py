import requests
from bs4 import BeautifulSoup
import json

#class scraper():    
def get_info():
    
    dct = {}

    with open('t.json') as ltt:
        dt = json.load(ltt)
        ltt.close()

    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
    
    try:
        notif_page = requests.get('https://ktu.edu.in/eu/core/announcements.htm', headers = headers)
    except:
        return dt["latest"], False

    soup_notif_page = BeautifulSoup(notif_page.text, 'html.parser')

    tr = soup_notif_page.findAll('tr')
    li = tr[1].findAll('li')

    final_text = "**New Notification**\n\n"

    #got the heading text in text 
    text = li[0].find('b').get_text()
    p = li[0].find('p').get_text()
    next = li[0].get_text().replace(text, "").replace(p,"")
    final_text += text + '\n\n' + next
    final_text += "\nFor more info : https://ktu.edu.in/eu/core/announcements.htm"

    dct["latest"] = final_text

    if dt["latest"] != final_text:
        with open('t.json', 'w') as lt:
            json.dump(dct, lt, indent = 4)
            lt.close()

        return final_text, True

    else:
        return dt["latest"], False
