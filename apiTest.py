import api as api
import json

apikey = "3ab92378-ea55-4dac-80f1-c8beb53b8c8c"
topic = "/users/Louis/ODI/airquality"

topic_data = api.messages_by_topic (apikey, topic)

print type(topic_data)

json_data = json.loads(topic_data)

print type(json_data)

messages = json_data["messages"]

print type(messages)

length = len(messages)

print length

print(messages[length-1])

print json_data["next"]

nexty  = "https://opensensors.io/api/1.0/users/Louis/messages-by-topic?start-date=" + messages[length-1]["date"] + "&topic=" + topic

print nexty

print api.connect (nexty,apikey).read()