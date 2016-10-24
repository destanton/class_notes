l = [1, "2", 3, 4, 'danielle', None]

string_list = str(l)
print(string_list)


import json

json_list = json.dumps(l)
print(json_list)

print(json.dumps({"danielle": 'codes'}))
