
import json
import requests
from datetime import datetime

from flask import Flask,request

app = Flask(__name__)


## http://127.0.0.1:5000/get_slots?state=uttar pradesh&district=bareilly&age_limit=45

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/get_slots',methods=['GET'])
def index():
	state_name=""
	district_name=""
	age_limit=""
	if 'state' in request.args:
		state_name = str(request.args['state'])
		district_name = str(request.args['district'])
		age_limit = int(request.args['age_limit'])
	state_url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
	res = requests.get(state_url)
	response = json.loads(res.text)	
	for ele in response["states"]:
		if ele["state_name"].lower()==state_name:
			state_id = ele["state_id"]
	
	district_url = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/"+str(state_id)
	res = requests.get(district_url)
	response = json.loads(res.text)		
	for ele in response["districts"]:
		if ele["district_name"].lower()==district_name:
			district_id = ele["district_id"]

	date = datetime.today().strftime('%d-%m-%Y')
	url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+str(district_id)+"&date="+date
	print("")
	res = requests.get(url)
	response = json.loads(res.text)
	centres_available=0
	html_text = "<html> <head> <title>Vaccine availability State "+state_name+" District: "+district_name+"</title> <body> <h2>Vaccine slots availability</h2> <table style=\"width:100%\" border=\"2\"> <tr>    <th>Date</th>    <th>Centre Name</th>    <th>Available seats</th>  </tr>"
	for ele in response["centers"]:
		for elem in ele["sessions"]: 
			if elem["min_age_limit"]==age_limit and elem["available_capacity"]>0:
				# line = "Date: "+elem["date"]+" Centre Name: "+ele["name"]+" Available seats: "+str(elem["available_capacity"])+"\n"
				# print(line)
				# text=text+line
				html_text = html_text+"<tr>    <th>"+elem["date"]+"</th>    <th>"+ele["name"]+"</th>    <th>"+str(elem["available_capacity"])+"</th>  </tr>"
				centres_available=centres_available+1
	html_text = html_text+ "</table>"
	html_text = html_text+ "<p> Available Centres: "+str(centres_available)+"</p>"
	html_text = html_text+ " </body> </html>"
	return html_text

if __name__=='__main__':
	app.run(debug=True)