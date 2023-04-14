

import json
file = open ("employee.json")
data = json.load(file)
for i in data ["employee_details"]:
    print(i)

file.close()

