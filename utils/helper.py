import json

def read_json_file(_filePath):   #put this in another separate file, exceptional handling
    with open(_filePath) as _user_file:
        _parsedJson = json.load(_user_file)
    return _parsedJson  

def write_json_file(_filepath, data):
    json_data = json.dumps(data, indent=4)
    with open(_filepath, 'w') as file:
        file.write(json_data)


