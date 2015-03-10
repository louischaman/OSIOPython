import apiSta as api
import json
from datetime import datetime

apikey = "f618fcef-f775-4c56-b1c6-f3b22dbb69bd"

topic_data = api.messages_by_topic (apikey, "/users/Louis/test2")

print type(topic_data)

json_data = json.loads(topic_data)

print type(json_data)

messages = json_data["messages"]

print type(messages)

print(messages[9])

print type(messages[9])

print messages[9]["device"]

dateStr = messages[7]['date']

print dateStr 

try:
    dt_start = datetime.strptime(dateStr, '%Y-%m-%dT%H:%M:%S.%fZ')
except ValueError:
    print "Incorrect format"




tt = dt_start.timetuple()
for it in tt:   
	print it

print json_data["next"]

# print api.connect (json _data["next"],apikey).read()