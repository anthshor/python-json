import subprocess
import json
import datetime

mydate = datetime.datetime.now().strftime("%Y-%m-%d")

myJson = subprocess.run(['oc','get','projects','-o','json'], stdout=subprocess.PIPE)
myJson.stdout.decode("utf-8")

myProjects = json.loads(str(myJson.stdout.decode("utf-8")))

filename = "project_list_" + mydate

f = open(filename, "w")
i=0
while (i<len(myProjects['items'])):
  f.write(str(myProjects['items'][i]['metadata']['name']) + "\n")
  i += 1
f.close()
