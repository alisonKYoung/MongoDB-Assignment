import pymongo
import json
import yaml

def validateStuff(needed_data):
    with open("schema.yaml", "r") as yaml_file:
        data = yaml.load(yaml_file, yaml.Loader)
    the_list = []
    for i in needed_data:
        the_list.append(i)
        for k in i:
            if type(i[k]) == type(data[k]):
                validated = True
            else:
                try:
                    the_list.remove(i)
                except:
                    continue
    return the_list