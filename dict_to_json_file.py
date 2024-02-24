import json

my_list = [1, "apple", True]
js_list = []

for i in my_list:
    fields = {"values": i}
    js_list.append(fields)
    
with open("final.json", "w") as obj:
    json.dump(js_list, obj)

print("JSON data has been written to file.txt")
