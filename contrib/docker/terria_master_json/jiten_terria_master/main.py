
from pathlib import Path
import json
import os
 
from flask import Flask
app = Flask('Terria Master JSON WebServer')

@app.route('/terriamasterjson')
def terriamasterjson’():
    return [1,2,3]


def getNewJsonData(fileName,groupIndex,granularityIndex,regionIDIndex,focusArr):
	fparam = fileName.split('_')
	# print(fparam)
	print(fileName)

	f = open('allCatalogueJson/{}'.format(fileName))
	data = json.load(f)
	# catalogue data
	i = data['catalog'][0]
	allResource = i["members"][0]["members"]

	if fparam[0] == 'FL':
		
		groIndex = groupIndex.index(fparam[3])
		if fparam[1] == 'FL':
			tempKey = fparam[1]+'_'+fparam[2]
			#print(tempKey)
			regIndex = regionIDIndex.index(tempKey)
			# regIndex = 8
		#print("-- if --")
		#focusArr[regIndex]['members'][groIndex]['members']
		#print(focusArr[regIndex]['name'], focusArr[regIndex]['members'][groIndex]['name'])

		mkey = 'members'
		if mkey in focusArr[regIndex]['members'][groIndex]:
			print("-- key exist if --")
			catalogContent = ''
			#print("exist key {}, in dic {}".format(mkey, focusArr[regIndex]['members'][groIndex]))
			catalogContent = {"name": i["members"][0]["name"], "type": "group", "description": "","isOpen": False, "members":allResource}
			focusArr[regIndex]['members'][groIndex]['members'].append(catalogContent)

		else:
			print("----  key not exist  in else--- ")

			catalogContent = []
			catalogContent.append({"name": i["members"][0]["name"], "type": "group", "description": "","isOpen": False, "members":allResource})
			focusArr[regIndex]['members'][groIndex]['members'] = catalogContent

	else:
		#print("-- else --")

		groIndex = groupIndex.index(fparam[2])
		regIndex = regionIDIndex.index(fparam[0])
		graIndex = granularityIndex.index(fparam[1])

		#print("graIndex - value {} - {}".format(graIndex, fparam[1]))

		mkey = 'members'
		if mkey in focusArr[regIndex]['members'][graIndex]['members'][groIndex]:
			#print("-- in If ---")
			catalogContent = ''
			catalogContent = {"name": i["members"][0]["name"], "type": "group", "description": "","isOpen": False, "members":allResource}
			focusArr[regIndex]['members'][graIndex]['members'][groIndex]['members'].append(catalogContent)		 
		else:
			#print("Not exist key {}, in dic {}".format(mkey, focusArr[regIndex]['members'][graIndex]['members'][groIndex]))
			#print("group name {}".format(focusArr[regIndex]['members'][graIndex]['members'][groIndex]['name']))
			#print("granularity name {}".format(focusArr[regIndex]['members'][graIndex]['name']))

			catalogContent = []
			catalogContent.append({"name": i["members"][0]["name"], "type": "group", "description": "","isOpen": False, "members":allResource})
			focusArr[regIndex]['members'][graIndex]['members'][groIndex]['members'] = list(catalogContent)

	return focusArr


regionIDColumns = {"DeSoto" : "DES", "Hillsborough":"HIL", "Manatee":"MAN", "Pinellas":"PIN", "Sarasota":"SAR","Florida Congressional Districts":"FL_CD","Florida House Districts":"FL_H", "Florida Senate Districts":"FL_Senate","Florida Counties":"FL_C"}

granulatiryColumns = {"Blocks":"B", "Block Groups":"BG", "Tracts":"T", "ZCTA":"ZIP", "Places":"P"}

#Group Name
colorColumns = {"Arts, Culture & Leisure" : "YlGn", "Basic Needs":"Reds", "Children & Families": "BuGn", "Civics & Public Safety":"BuPu", "Economy":"YlOrBr", "Education":"Oranges", "Equity & Equality": "RdPu", "Health":"Purples", "Housing":"PuBuGn", "People":"PuRd", "Sustainability":"Greens", "Transportation":"YlOrRd"}


regionIDIndex = []
granularityIndex = []
groupIndex = []



regionIDIndex = []
granularityIndex = []
groupIndex = []

for index, (key, value) in enumerate(colorColumns.items()):
	groupIndex.append(key)

for index, (key, value) in enumerate(granulatiryColumns.items()):
	granularityIndex.append(value)

for index, (key, value) in enumerate(regionIDColumns.items()):
	regionIDIndex.append(value)


focusArr = []
for index, (key, value) in enumerate(regionIDColumns.items()):
	
	granularityArr = []
	if value == 'FL_CD' or value == 'FL_h' or value == 'FL_Senate' or value == 'FL_C': 
		themeArr = []
		for index1, (key1, value1) in enumerate(colorColumns.items()):
			theme = {"name": key1, "type": "group", "description": "", "isOpen": False}
			themeArr.append(dict(theme))
		focus = {"name":key,"type":"group","description":"","isOpen":False, 'members':themeArr }
		focusArr.append(dict(focus))
	else:

		for index2, (key2, value2) in enumerate(granulatiryColumns.items()):
			themeArr = []
			for index1, (key1, value1) in enumerate(colorColumns.items()):
				theme = {"name": key1, "type": "group", "description": "", "isOpen": False}
				themeArr.append(dict(theme))

			granularity = {"name": key2, "type": "group", "description": "", "isOpen": False, "members": themeArr}
			granularityArr.append(dict(granularity))

		focus = {"name":key,"type":"group","description":"","isOpen":False, 'members':granularityArr}
		focusArr.append(dict(focus))

# by default it consider current directory
path = "allCatalogueJson"
counter = 1
for fileName in os.listdir(path):
	 print("{} -- Reading Files:{}".format(counter, fileName))
	 focusArr = getNewJsonData(fileName,groupIndex,granularityIndex,regionIDIndex,focusArr)
	 counter = counter + 1
# fileName = 'FL_FL_CD_Basic Needs_2010.json'
# fileName = 'DES_BG_Basic Needs_2010.json'



 
groupInfo = {"name": "Focus", "type": "group", "description": "Focus description","isOpen": False, "members":focusArr}

basemapInfo = {
                "items": [
                            {
                            "item": {
                              "id": "test-basemap",
                              "name": "Voyager with labels",
                              "type": "open-street-map",
                              "url": "https://basemaps.cartocdn.com/rastertiles/voyager_labels_under/",
                              "attribution": "© <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a>, © <a href='https://carto.com/about-carto/'>CARTO</a>",
                              "subdomains": ["a", "b", "c", "d"],
                              "opacity": 1.0
                            },
                            "image": "build/TerriaJS/images/Australia.png"
                          }
                        ],
                "defaultBaseMapId": "basemap-positron",
                "previewBaseMapId": "basemap-positron",
            }
catalogJson = dict()
catalogJson["homeCamera"] = {"north": 31.0, "east": -80.0,"south": 24.5, "west": -87.6}
catalogJson["catalog"] = [groupInfo]
catalogJson["viewerMode"] = "3dSmooth"
catalogJson["baseMaps"] = basemapInfo

fle = Path('masterTerriaCatalogue.json')
fle.touch(exist_ok=True)

with open(fle, 'w+') as fp:
    json.dump(catalogJson, fp)
