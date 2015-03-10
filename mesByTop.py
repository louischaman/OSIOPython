import api
import json

apikey = "3ab92378-ea55-4dac-80f1-c8beb53b8c8c"

topic_data = api.messages_by_topic (apikey, "/users/andylockran/ElectricityUsage")

print type(topic_data)

json_data = json.loads(topic_data)

print type(json_data)

messages = json_data["messages"]

print type(messages)

print json_data["next"]

print api.connect (json_data["next"],apikey)