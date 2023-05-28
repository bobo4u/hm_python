import json
file= "username.json"

try:
    with open(file) as f:
        username = json.load(f)

except FileNotFoundError:
    username = input("请输入名称：")
    with open(file,"w") as f:
        json.dump(username,f)
        print(f"{username}")
else:
    print(f"hi {username}")