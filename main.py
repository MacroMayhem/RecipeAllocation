from source.RecipeAllocator import RecipeAllocator
from flask import Flask
import flask
app = Flask(__name__)
from flask import request
import json

__author__ = "Aditya Singh"
__version__ = "0.1.0"

@app.route("/allocate",methods =['GET'])
def allocate():
    try:
        query = request.get_json()
        recipieAllocator = RecipeAllocator(orders_data=query['orders'],stock_data=query['stock'])
    except:
        return ('Possibly invalid request! Parsing Failure')
    try:
        return json.dumps(recipieAllocator.compute())
    except Exception as e:
        return ('Error in computing the allocation',e)

if __name__ == "__main__":
    app.run(port=9090,debug=True)