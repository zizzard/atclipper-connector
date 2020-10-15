from flask import  Flask, request
from flask_cors import CORS
from PreprocessingFunction import processMappedFile
import os

app = Flask(__name__)
CORS(app)

@app.route('/query', methods=['POST'])
def query():
    content = request.json

    print(content)
    ## TODO: Add Python script method here
    return content

@app.route('/add', methods=['POST'])
def add():
    form = request.form
    files = request.files

    try:
        jurisdiction = form["jurisdiction"]
        reportDate = form["reportDate"]
        mapping = form["mapping"]
        file = files["data"]
    except:
        return {"failure": 'failure'}

    print(jurisdiction)
    print(reportDate)
    print(mapping)
    print(file)

    processMappedFile(mapping, file, jurisdiction)

    return {"success": 'success'}
