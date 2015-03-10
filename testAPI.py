import api

apikey = "3ab92378-ea55-4dac-80f1-c8beb53b8c8c"

print("----------- I am -----------")

print api.whoami(apikey)

print("----------- my Devices are -----------")

print api.list_devices(apikey)

print ("----------- my Topics are -----------")

print api.list_topics(apikey)

print ("----------- messages by owner -----------")

print api.messages_by_owner(apikey, "Louis")

print ("----------- messages by topic -----------")

print api.messages_by_topic (apikey, "/users/andylockran/ElectricityUsage")
