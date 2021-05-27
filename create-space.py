# Fill in this file with the people listing code from the Webex Teams exercise
import requests
import json
from os import walk
access_token= "YTg0NmQxMzEtYmM4Ny00YTkwLWI3OTYtNTlhMDEwNDJiYzA1Y2E2ZWM2YTktNmEz_PF84_consumer"
#person_id="Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hYjJjZTU2NC1hNzliLTQ5YzUtODIzYS05MmNlYzQ5NjI5MGY"

def createSpace():
    url="https://webexapis.com/v1/rooms"
    headers= {
            "Authorization":"Bearer {}".format(access_token),
            "Content-Type":"application/json"
        }
    params ={"title":"netacad_devasc_skills_ND"}
    resp= requests.post(url,headers=headers,json=params)
    print(json.dumps(resp.json(),indent=4))
    print(resp.status_code)

def addMember(id):
    person_email="Yvan.rooseleer@biasc.be"
    room_id=id
    url="https://webexapis.com/v1/memberships"


    headers= {
            "Authorization":"Bearer {}".format(access_token),
            "Content-Type":"application/json"
        }
    params ={"roomId":room_id,"personEmail":person_email}
    resp= requests.post(url,headers=headers,json=params)
    print(json.dumps(resp.json(),indent=4))
    print(resp.status_code)
def getRooms():
    
    headers= {
            "Authorization":"Bearer {}".format(access_token),
            "Content-Type":"application/json"
        } 
    roomid="" 
    roomsurl="https://webexapis.com/v1/rooms"
    resp=requests.get(roomsurl,headers=headers)
    rooms=resp.json()
    for i in rooms["items"]:
        title=i["title"]
        if title =="netacad_devasc_skills_ND":
            roomid=i["id"]
    return roomid
    #print(rooms['items'])
def postFiles(room_id):
    messageurl= "https://webexapis.com/v1/messages"
    f = []
    mypath=".//"
    for (dirpath,dirnames,filenames) in walk(mypath):
        f.extend(filenames)
        for i in f:
            if ".png" in i:
            
                m = MultipartEncoder({'roomId': room_id,
                      'text': 'example attached',
                      'files':(i, open(i, 'rb'),
                      'image/png')})
                headers= {
            "Authorization":"Bearer {}".format(access_token),
            "Content-Type":m.content_type
             } 
                resp=requests.post(messageurl,headers=headers,data=m)
                print(resp.status_code)    

def postMessage(room_id)
    
    message = "Here are my screenshots of netacad-devasc skills-based exam"
    url = 'https://webexapis.com/v1/messages'
    headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
    }
    params = {'roomId': room_id, 'text': message}
    res = requests.post(url, headers=headers, json=params)
    print(res.json())

if __name__ == "__main__":
    createSpace()
    roomid=getRooms()
    addMember(roomid)      
    postMessage(roomid)
    postFiles(roomid)
