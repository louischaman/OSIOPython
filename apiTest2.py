import api as api
import json
from datetime import datetime


import plotly.plotly as py
from plotly.graph_objs import *

apikey = "3ab92378-ea55-4dac-80f1-c8beb53b8c8c"
topic = "/users/Louis/ODI/airquality"

topic_data = api.messages_by_topic (apikey, topic)

Data0 = []
Dates = []

def checkentry(message):
	dataOK = 0;
	# print me
	PMData ={}
	if me['device']=='964':
		dataOK = 1;
	dateStr = me['date']
	try:
		dt_start =  datetime.strptime(dateStr, '%Y-%m-%dT%H:%M:%S.%fZ')
	except ValueError:
		dataOK = 0;
	else :
		pass
	payloadStr = me['payload']
	if dataOK:
		try:
			PMData = json.loads(payloadStr["text"])
			PMData['date']=dt_start
		except ValueError, e:
			pass
		else:
			pass
		
	return PMData


messages = [1, 1]

while len(messages)>1:
	json_data = json.loads(topic_data)
	messages = json_data["messages"]
	length = len(messages)
	for me in messages:
		PMData = checkentry(me)
		if PMData:
			#datelist = datelist + [dt_start]
			pm2 = PMData["PM2.5 Count"]
			date = PMData["date"]
			Dates = Dates + [date]
			Data0 = Data0 + [pm2]
	nexty  = "https://opensensors.io/api/1.0/users/Louis/messages-by-topic?start-date=" + messages[length-1]["date"] + "&topic=" + topic
	topic_data =  api.connect (nexty,apikey).read()
AVGdata =[]
AVGdate =[]
smoothF = 10
for i in range(0,int(len(Data0)/smoothF)):
	toMean = [Data0[x] for x in range(i*smoothF,i*smoothF+smoothF-1)]
	AVGdata = AVGdata + [sum(toMean)/smoothF]
	AVGdate = AVGdate + [Dates[i*smoothF]]





trace1 = Scatter(
	x = AVGdate,
	y = AVGdata
)

data = Data([trace1])

plot_url = py.plot(data)