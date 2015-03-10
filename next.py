import api as api
import json

apikey = "3ab92378-ea55-4dac-80f1-c8beb53b8c8c"

topic_data = api.messages_by_topic (apikey, "/users/Louis/ODI/airquality")



json_data = json.loads(topic_data)

print json_data

nextAddress = json_data["next"]


print nextAddress

print api.connect (json_data["next"],apikey).read()