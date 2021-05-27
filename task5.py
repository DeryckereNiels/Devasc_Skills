import json
import requests
requests.packages.urllib3.disable_warnings()
basicauth=("cisco","cisco123!")
def deleteData():
    
    api_url = "https://192.168.56.101/restconf/data/Cisco-IOS-XE-native:native/logging/monitor"

    headers = {"Accept":"application/yang-data+json",
           "Content-type":"application/yang-data+json"
          }
   
    resp=requests.delete(api_url,auth=basicauth,headers=headers, verify=False)
    print ("-2- DELETE")
    print ("Statuscode: "+ str(resp.status_code))
    if (resp.status_code>=200 and resp.status_code <= 299):
        print (str(resp.headers)+ "\n")
    else: print ("no data to show")
def getOptions():
    api_url = "https://192.168.56.101/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity"

    headers = {"Accept":"application/yang-data+json",
           "Content-type":"application/yang-data+json"
          }
   
    resp=requests.options(api_url, auth=basicauth,headers=headers, verify=False)
    print ("-1- OPTIONS")
    if (resp.status_code>=200 and resp.status_code <= 299):
        print (str(resp.headers)+ "\n")
    else: print (resp.json())
    #print(json.dumps(resp,indent=4))

def postData():
    
    api_url = "https://192.168.56.101/restconf/data/Cisco-IOS-XE-native:native/logging/monitor"

    headers = {"Accept":"application/yang-data+json",
           "Content-type":"application/yang-data+json"
          }
    data= {"Cisco-IOS-XE-native:severity": "alerts"}
   
    resp=requests.post(api_url,data=json.dumps(data),auth=basicauth,headers=headers, verify=False)
    print ("-2- POST")
    print ("Statuscode: "+ str(resp.status_code))
    if (resp.status_code>=200 and resp.status_code <= 299):
        print (str(resp.headers)+ "\n")
    else: print (resp.json())
    #print (str(resp.headers)+ "\n")

def putData():
    
    api_url = "https://192.168.56.101/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity"

    headers = {"Accept":"application/yang-data+json",
           "Content-type":"application/yang-data+json"
          }
    data= {"Cisco-IOS-XE-native:severity": "alerts"}
   
    resp=requests.put(api_url,data=json.dumps(data),auth=basicauth,headers=headers, verify=False)
    print ("-3- PUT")
    print ("Statuscode: "+ str(resp.status_code))
    if (resp.status_code>=200 and resp.status_code <= 299):
        print (str(resp.headers)+ "\n")
    else: print (resp.json())
    print (resp.headers)
def getData():
    
    api_url = "https://192.168.56.101/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity"

    headers = {"Accept":"application/yang-data+json",
           "Content-type":"application/yang-data+json"
          }
   
    resp=requests.get(api_url,auth=basicauth,headers=headers, verify=False)
    print ("-5- GET")
    print ("Statuscode: "+ str(resp.status_code))
    if (resp.status_code>=200 and resp.status_code <= 299):
        print (str(resp.headers)+ "\n")
    else: print ("No data to show")
    #print (resp.json())

def patchData():
    
    api_url = "https://192.168.56.101/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity"

    headers = {"Accept":"application/yang-data+json",
           "Content-type":"application/yang-data+json"
          }
    data= {"Cisco-IOS-XE-native:severity": "warnings"}
   
    resp=requests.patch(api_url,data=json.dumps(data),auth=basicauth,headers=headers, verify=False)
    print ("-4- PATCH")
    print ("Statuscode: "+ str(resp.status_code))
    if (resp.status_code>=200 and resp.status_code <= 299):
        print (str(resp.headers)+ "\n")
    else: print (resp.json())
    #print (str(resp.headers)+ "\n")

if __name__ == "__main__":
    getOptions()
    postData()
    putData()
    patchData()
    getData()
    deleteData()
