# SAMPLE 3 - READ FROM ODATA 4.0 from Python RS, 09032019

# LOAD PHYTON MODULES
import requests
from requests.auth import HTTPDigestAuth
from requests_ntlm import HttpNtlmAuth
from requests.auth import HTTPBasicAuth
import json
 
# AUTH MODE - LOGIN\PASSWORD (USERS AND WEB SERVICES KEY)
# auth=HTTPBasicAuth(username,userpassword) -> Autentication Module
username = 'usernama' #username
userpassword = 'service key' #password
 
#set these values to query your Dynamics 365 Business Central Company-OData (Page or Query exposed as Odata 4.0)
BCapi = 'https://api.businesscentral.dynamics.com/v1.0/tenant/ODataV4/Company('"'CRONUS_IT'"')' #full path to web api endpoint
#web api query part(include leading /): example - Item List No, Description
BCapiquery = '/ItemList?$select=No,Description, Inventory'
 

# GET DATA (BY REQUEST METHOD)
r = requests.get(BCapi+BCapiquery, auth=HTTPBasicAuth(username,userpassword),
       headers = {
        'OData-MaxVersion': '4.0',
        'OData-Version': '4.0',
        'Accept': 'application/json',
        'Content-Type': 'application/json; charset=utf-8',
        'Prefer': 'odata.maxpagesize=500',
        'Prefer': 'odata.include-annotations=OData.Community.Display.V1.FormattedValue'        
    })
    
try:
        #get the response (Json object)
        getData = r.json()
 
        #loop in response (No, Description)
        for x in getData['value']:
            print (x['No'] + ' - ' + x['Description'] + ' - ' + str(x['Inventory']))
            
except KeyError:
        #handle any missing key errors

# PRINT DATA   
        print('Errors retreiving data from Business Central')

#QUIT

