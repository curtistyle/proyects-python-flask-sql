import requests
from flask import request

def input_band():
    name = request.args['name']
    print(name)
    
def output_band(band):
    

