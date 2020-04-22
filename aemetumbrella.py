import xml.etree.ElementTree as ET
import requests

def get_precip_info(day, hour):

    #The data is in four periods 00-06, 06-12, 12-18 and 18-24
    hourtag_list = []
    if(int(hour)<6):
	hourtag_list.append("00-06")
    if(int(hour)<12):
        hourtag_list.append("06-12")
    if(int(hour)<18):
        hourtag_list.append("12-18")
    if(int(hour)<24):
        hourtag_list.append("18-24")

    req_str = "http://www.aemet.es/xml/municipios/localidad_28092.xml"
    
    print "Fetching AEMET..."
    req = requests.get(req_str)
   
    tree = ET.fromstring(req.text.encode('utf-8'))
    treeDay = None
    for dia in tree.iter("dia"):
        if(dia.get("fecha")==day):	    
            treeDay = dia

    if(treeDay is None):
        return -1

    for prob in treeDay.iter("prob_precipitacion"):
        if(prob.get("periodo") in hourtag_list):
            print "Day: " + day + " Period: " + prob.get("periodo") + " Prob: " + prob.text
            if(int(prob.text)>49):
                return 1
    return 0
		    
