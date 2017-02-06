import requests
import json

#apic_em_ip = "https://sandboxapic.cisco.com/api/v1"

def get_token(url):

    #Define API call
    api_call = "/ticket"

    # Payload contains authentication information
    payload = {"username": "devnetuser", "password": "Cisco123!"}

    # Header information
    headers = {
        "content-type": "application/json"
    }

    #combine url and API call
    url += api_call

    ticket = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)

    return ticket

def get_device_id(token, url):

    #define API call
    api_call = "/network-device"

    #header info
    headers = {"X-AUTH-TOKEN": token}

    url += api_call

    response = requests.get(url, headers=headers, verify=False).json()

    #iterate through response looking for the ACCESS role.
    for item in response['response']:
        if item['role'] == 'ACCESS':
            return item['id']

def get_config(token, url, id):

    #define API call
    api_call = '/network-device/' + id + '/config'
    print (api_call)
    #headers
    headers = {'X-AUTH-TOKEN': token}
    print (headers)

    url += api_call
    print (url)

    response = requests.get(url, headers=headers, verify=False).json()

    return response