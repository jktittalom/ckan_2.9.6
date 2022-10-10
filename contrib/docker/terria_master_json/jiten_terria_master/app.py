from pathlib import Path
import json
import os


from flask import Flask
app = Flask('Terria Master JSON WebServer')


@app.route('/')
def index():
    return "Welcome Jiten!!"


@app.route('/test')
def test():
    print("test Welcome!!!")
    # /usr/lib/ckan/terria_catalog
    hpath = Path.home()
    cpath = Path.cwd()
    return "hello test cpath: {}, home: {}".format(cpath, hpath)


def getNewJsonData(fileName, groupIndex, granularityIndex, regionIDIndex, focusArr):
    fparam = fileName.split('_')

    cpath = Path.cwd()
    f = open('{}/allCatalogueJson/{}'.format(cpath, fileName))
    # cpath = '/usr/lib/ckan/terria_catalog/'
    # f = open('{}/allCatalogueJson/{}'.format(cpath,fileName))
    #return "file path name:{}".format(f)
    data = json.load(f)
    # catalogue data
    i = data['catalog'][0]
    allResource = i["members"][0]["members"]

    if fparam[0] == 'FL':

        groIndex = groupIndex.index(fparam[3])
        if fparam[1] == 'FL':
            tempKey = fparam[1]+'_'+fparam[2]
            # print(tempKey)
            regIndex = regionIDIndex.index(tempKey)

        mkey = 'members'
        if mkey in focusArr[regIndex]['members'][groIndex]:
            # print("-- key exist if --")
            catalogContent = ''
            catalogContent = {"name": i["members"][0]["name"], "type": "group",
                              "description": "", "isOpen": False, "members": allResource}
            focusArr[regIndex]['members'][groIndex]['members'].append(
                catalogContent)

        else:
            # print("----  key not exist  in else--- ")
            catalogContent = []
            catalogContent.append({"name": i["members"][0]["name"], "type": "group",
                                  "description": "", "isOpen": False, "members": allResource})
            focusArr[regIndex]['members'][groIndex]['members'] = catalogContent

    else:
        # print("-- else --")

        groIndex = groupIndex.index(fparam[2])
        regIndex = regionIDIndex.index(fparam[0])
        graIndex = granularityIndex.index(fparam[1])

        # print("graIndex - value {} - {}".format(graIndex, fparam[1]))

        mkey = 'members'
        if mkey in focusArr[regIndex]['members'][graIndex]['members'][groIndex]:
            # print("-- in If ---")
            catalogContent = ''
            catalogContent = {"name": i["members"][0]["name"], "type": "group",
                              "description": "", "isOpen": False, "members": allResource}
            focusArr[regIndex]['members'][graIndex]['members'][groIndex]['members'].append(
                catalogContent)
        else:
            # print("Not exist key {}, in dic {}".format(mkey, focusArr[regIndex]['members'][graIndex]['members'][groIndex]))
            # print("group name {}".format(focusArr[regIndex]['members'][graIndex]['members'][groIndex]['name']))
            # print("granularity name {}".format(focusArr[regIndex]['members'][graIndex]['name']))

            catalogContent = []
            catalogContent.append({"name": i["members"][0]["name"], "type": "group",
                                  "description": "", "isOpen": False, "members": allResource})
            focusArr[regIndex]['members'][graIndex]['members'][groIndex]['members'] = list(
                catalogContent)

    return focusArr


@app.route('/masterjson')
def masterjson():
    regionIDColumns = {"DeSoto": "DES", "Hillsborough": "HIL", "Manatee": "MAN", "Pinellas": "PIN", "Sarasota": "SAR",
                       "Florida Congressional Districts": "FL_CD", "Florida House Districts": "FL_H", "Florida Senate Districts": "FL_Senate", "Florida Counties": "FL_C"}

    granulatiryColumns = {"Blocks": "B", "Block Groups": "BG",
                          "Tracts": "T", "ZCTA": "ZIP", "Places": "P"}

    # Group Name
    colorColumns = {"Arts, Culture & Leisure": "YlGn", "Basic Needs": "Reds", "Children & Families": "BuGn", "Civics & Public Safety": "BuPu", "Economy": "YlOrBr",
                    "Education": "Oranges", "Equity & Equality": "RdPu", "Health": "Purples", "Housing": "PuBuGn", "People": "PuRd", "Sustainability": "Greens", "Transportation": "YlOrRd"}

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
    #return "master Json"

    for index, (key, value) in enumerate(regionIDColumns.items()):
        granularityArr = []

        if value == 'FL_CD' or value == 'FL_h' or value == 'FL_Senate' or value == 'FL_C':
            themeArr = []
            for index1, (key1, value1) in enumerate(colorColumns.items()):
                theme = {"name": key1, "type": "group",
                         "description": "", "isOpen": False}
                themeArr.append(dict(theme))
            focus = {"name": key, "type": "group", "description": "",
                     "isOpen": False, 'members': themeArr}
            focusArr.append(dict(focus))
        else:

            for index2, (key2, value2) in enumerate(granulatiryColumns.items()):
                themeArr = []
                for index1, (key1, value1) in enumerate(colorColumns.items()):
                    theme = {"name": key1, "type": "group",
                             "description": "", "isOpen": False}
                    themeArr.append(dict(theme))

                granularity = {"name": key2, "type": "group",
                               "description": "", "isOpen": False, "members": themeArr}
                granularityArr.append(dict(granularity))

            focus = {"name": key, "type": "group", "description": "",
                     "isOpen": False, 'members': granularityArr}
            focusArr.append(dict(focus))
            # by default it consider current directory
    #return "master Json111"
    cpath = Path.cwd()
    path = "{}/allCatalogueJson".format(cpath)
    counter = 1
    for fileName in os.listdir(path):
        # print("{} -- Reading Files:{}".format(counter, fileName))
        focusArr = getNewJsonData(fileName, groupIndex, granularityIndex, regionIDIndex, focusArr)
        counter = counter + 1

    groupInfo = {"name": "Focus", "type": "group",
                 "description": "Focus description", "isOpen": False, "members": focusArr}
    #return "master Json222 members:{}".format(focusArr)
    basemapInfo = {
        "items": [
            {
                "item": {
                    "id": "test-basemap",
                    "name": "Voyager with labels",
                    "type": "open-street-map",
                    "url": "https://basemaps.cartocdn.com/rastertiles/voyager_labels_under/",
                    "attribiution": "© <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a>, © <a href='https://carto.com/about-carto/'>CARTO</a>",
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
    catalogJson["homeCamera"] = {"north": 31.0,
                                 "east": -80.0, "south": 24.5, "west": -87.6}
    catalogJson["catalog"] = [groupInfo]
    catalogJson["viewerMode"] = "3dSmooth"
    catalogJson["baseMaps"] = basemapInfo

    fle = Path('{}/masterTerriaCatalogue.json'.format(cpath))
    fle.touch(exist_ok=True)
    with open(fle, 'w+') as fp:
        json.dump(catalogJson, fp)
    return "{}".format(catalogJson)
