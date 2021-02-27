import requests,json
response = requests.get('https://api.ivao.aero/getdata/whazzup/') 
whazzup = (response.text)
lines = whazzup.split("!CLIENTS")[-1].split("!AIRPORTS")[0]
for line in lines.split('\n'):
	headings = ["Callsign","VID","Name","Client Type","Frequency","Latitude","Longitude","Altitude","Groundspeed","Flight Plan","Filed Cruise Speed","Departure Airport","Filed Flight Level","Destination","Server","Protocol","Rating","Squawk Code","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","ATIS"]
	dictionary = dict(zip(headings, line.split(':')))
	try:
		keys_to_remove = ["Flight Plan","Protocol"]
		for i in range(1,16):
			keys_to_remove.append(str(i))
		for key in keys_to_remove:
		  del dictionary[key]
	except:
		pass
	if len(list(dictionary.keys()))>=17:
		print(json.dumps(dictionary, indent=4))