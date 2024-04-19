import json

dict = {}

with open('path\\to\\file', 'w') as file:
    file.write(json.dumps(dict))