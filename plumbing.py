import requests
import uuid
import json

def flush(list_str_recordings):
    uuid_str = str(uuid.uuid4())[:5]

    measure_set = []
    print(list_str_recordings)
    for i in range(0, len(list_str_recordings)-2):
        measure_set.append(list_str_recordings[i])

    pre_json = {'uuid':uuid_str, 'measure_set':measure_set}
    json_request = json.dumps(pre_json)

    pre_log = [{"status":0}, {"request_body":json_request}]
    json_log = json.dumps(pre_log)
    with open('log.txt', 'r+') as log:
        before_log = log.read()
        log.write(before_log+"\n\n"+json_log)
    
        
    
