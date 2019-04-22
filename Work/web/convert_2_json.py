import json 
import sys
input_file = sys.argv[1]
json_file = './server/apache-tomcat-9.0.11/webapps/visualization/test.json'
temp_dict = {}
line_number = 1 
with open( input_file ) as f:
    line = f.readline().strip()
    while line:
        temp_dict[line_number] = line
        line = f.readline().strip()
        line_number += 1
json.dump(temp_dict, open(json_file, 'w'))    


