import requests
import json
from django.http import HttpResponse


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
        if item['role'] == 'UNKNOWN':
            return item['id']

def get_config(token, url, id):
    #define API call
    api_call = '/network-device/' + id + '/config'
    #headers
    headers = {'X-AUTH-TOKEN': token}

    url += api_call

    response = requests.get(url, headers=headers, verify=False).json()
    return response

def return_dict_example(apic_em_ip):
    auth_token = get_token(apic_em_ip)
    auth_token = json.loads(HttpResponse.getvalue(auth_token).decode('utf-8'))
    auth_token = auth_token['response']['serviceTicket']
    device_id = get_device_id(auth_token, apic_em_ip)
    config = get_config(auth_token, apic_em_ip, device_id)

    return config
