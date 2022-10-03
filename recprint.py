# Recursively access JSON object to access each value at a time.
def recursivePrintJson(jobj):
    if type(jobj) is list:
        for list_item in jobj:
            recursivePrintJson(list_item)
    elif type(jobj) is dict:
        for k, v in jobj.items():
            if type(v) is not list and type(v) is not dict:
                print(v)
            else:
                recursivePrintJson(v)
    else:
        print(jobj)
