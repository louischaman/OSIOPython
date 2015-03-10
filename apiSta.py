import urllib
import urllib2
import requests

base_url = "https://staging.opensensors.io/api/1.0"

def connect (url, apikey):
    req = urllib2.Request (url)
    req.add_header ("Authorization", "api-key " + apikey)
    return urllib2.urlopen (req)

def whoami (apikey):
    url = base_url + "/whoami"
    return connect (url, apikey).read ()

def list_devices (apikey):
    url = base_url + "/users/" + whoami (apikey) + "/devices/"
    return connect (url, apikey).read ()

def list_topics (apikey):
    url = base_url + "/users/" + whoami (apikey) + "/topics/"
    return connect (url, apikey).read ()
    
def create_device (apikey):
    url = base_url + "/users/" + whoami (apikey) + "/devices/"
    requests.post (url, data= {}, headers='Authorization: apikey ' + apikey)

#get messages
def messages_by_owner (apikey, owner, **kwargs):
    '''find messages published by particular users
    keyword arguments startdate and/or enddate narrow by date

    examples:
    api.messages_by_owner(apikey, userid)
    api.messages_by_owner(apikey, userid, startdate='2014-11-20', enddate='2014-11-24')
    '''
    if 'startdate' and 'enddate' in kwargs:
        url = base_url + "/users/" + owner + "/messages-by-owner?start-date=" + kwargs ['startdate'] + "&&end-date=" + kwargs ['enddate']
    elif 'startdate' in kwargs:
        print ("boo")
        url = base_url + "/users/" + owner + "/messages-by-owner?start-date=" + kwargs ['startdate']
    else: url = base_url + "/users/" + owner + "/messages-by-owner"
    return connect (url, apikey).read ()


    
def messages_by_topic (apikey, topic):
    url = base_url + "/users/" + whoami (apikey) + "/messages-by-topic?topic=" + topic
    return connect (url, apikey).read ()
