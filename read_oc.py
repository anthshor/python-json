import subprocess
import json

myJson = subprocess.run(['oc','get','projects','-o','json'], stdout=subprocess.PIPE)

myJson.stdout.decode("utf-8")
#print(str(myJson.stdout.decode("utf-8")))

myProjects = json.loads(str(myJson.stdout.decode("utf-8")))


print(myProjects.items.kind)