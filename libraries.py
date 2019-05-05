# import json

# def GenerateJson(context_data, session_name, session_venue, session_lecturer):
#     output = context_data
#     output.update({session_name : [session_venue, session_lecturer]})
#     output = json.dumps(output)
#     return(output)

import json

def load_json():
    x = None

def is_json(json_file):
    try:
        json_object = json.loads(json_file)
    except:
        return False
    return True