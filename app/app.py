
from flask import Flask,request,jsonify
from pathlib import Path
import os
from werkzeug.utils import secure_filename
import boto3
from boto3.session import Session
from botocore.exceptions import ClientError
from flask import send_from_directory


# from nltk.corpus import stopwords
#===================================================================================================================================

app = Flask(__name__)
                            #initilaze the flask application



@app.route("/health",methods=['GET'])
def pdf_upload_lattice():
    return "hello in My flask world"











#=============================================================================================================================================
if __name__ == '__main__':
    print("--------------------------------------------------------")
    app.run(threaded=True, debug=False, host='127.0.0.1', port=5000)
