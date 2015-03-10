import api as api
import json
from datetime import datetime

def checkentry(message):

	dataOK = 0;
	# print me
	PMData =[]
	if me['device']=='964':
		dataOK = 1;
		print 'device ok'
	else:
		print 'bad device'

	dateStr = me['date']
	try:
		dt_start =  datetime.strptime(dateStr, '%Y-%m-%dT%H:%M:%S.%fZ')
	except ValueError:
		dataOK = 0;
		print "bad date"
	else :
		print "date ok"
		pass

	payloadStr = me['payload']
	if dataOK:
		try:
			PMData = json.loads(payloadStr["text"])
		except ValueError, e:
			print "bad payload"
		else:
			print "payload ok"
			pass

	return PMData


apikey = "3ab92378-ea55-4dac-80f1-c8beb53b8c8c"

topic_data = api.messages_by_topic (apikey, "/users/Louis/ODI/airquality")

json_data = json.loads(topic_data)

messages = json_data["messages"]

datelist = []
data1= []
data2= []

for me in messages:

	PMData = checkentry(me)
	if PMData:
		#datelist = datelist + [dt_start]
		print PMData

