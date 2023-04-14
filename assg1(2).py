


import json 
      
# Data to be written 
dictionary ={ 
            "TamilNadu":"Chennai",
            "Kerala":"Trivandrum",
            "Karnataka":"Bengaluru",
            "Telungana":"Hyderabad",
            "Maharashtra":"Mumbai",
            "Andhra Pradesh":"Amaravati",
            "Goa":"Panaji"
  
} 
      
# Serializing json  
json_object = json.dumps(dictionary) 
print(json_object)