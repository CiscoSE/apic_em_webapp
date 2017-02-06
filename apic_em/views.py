from django.http import HttpResponse
import requests
import json
from .get_stuff import get_token, get_config, get_device_id


#Disable SSL warning
requests.packages.urllib3.disable_warnings()

# Create your views here.

apic_em_ip = "https://sandboxapic.cisco.com/api/v1"
catfacts_ip = 'http://catfacts-api.appspot.com/api'

def practice(request):

    requests.packages.urllib3.disable_warnings()
    api_call = "/facts"
    url = catfacts_ip + api_call
    header = '"text/html; charset=utf-8"'

    #get the cat fact - type will return as requests.models.Response
    my_response = requests.get(url, params='number=5', verify=False)

    #take the "utf-8" response value and convert it to a json disctionary
    data = json.loads(HttpResponse.getvalue(my_response).decode('utf-8'))

    #save one of the facts out to a variable
    response = data['facts'][0]

    return HttpResponse(response)

def index(request):

    auth_token = get_token(apic_em_ip)
    print (type(auth_token))
    #auth_token = json.loads(HttpResponse.getvalue(auth_token).decode('utf-8'))
    #auth_token = auth_token['response']['serviceTicket']
    #device_id = get_device_id(auth_token, apic_em_ip)
    #print (type(device_id))
    #device_id = json.loads(HttpResponse.getvalue(device_id).decode('utf-8'))
    #config = get_config(auth_token, apic_em_ip, device_id)
    #print (type(config))
    #config = json.loads(HttpResponse.getvalue(config).decode('utf-8'))

    return HttpResponse('Hello, world.')