import json

with open('input/authme.json') as json_file:
    jsondata = json.load(json_file)
    for data in jsondata:
        if(data['email']):
            fileinput = "{email}:{password}".format(email = data['email'], password = data['password'])
            print(fileinput)
            postName = data['email'][data['email'].find("@") + 1:]
            outputFile = open("output/" + postName + ".txt", "a")
            outputFile.write(fileinput + "\n")
            outputFile.close()
