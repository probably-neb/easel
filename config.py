import json

config_file = open("easel.json", 'r')
config = json.loads(config_file.read())

domain = config["info"]["domain"]
token = config["info"]["token"]

def get_domain():
    return domain

def get_token():
    return token

def get_config():
    return config
