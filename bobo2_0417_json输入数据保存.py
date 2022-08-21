import json

username = input("please input u name:")
filename = "username.json"
with open(filename,"w") as f:
    json.dump(username,f)
    print(f"i kowm u name,{username}")

with open(filename) as files:
    name1 = json.load(files)
    print(f"wow come back {name1}")