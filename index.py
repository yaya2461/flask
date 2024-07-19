import mimetypes
import os
from flask import Flask, send_file
from flask import request, jsonify
import cv2
import numpy as np
from ultralytics import YOLO
import matplotlib.pyplot as plt
import math
from flask import Flask, request
from flask_restful import Api, Resource
from flask import Flask, jsonify
from flask_cors import CORS
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)


   
@app.route('/test', methods=['GET'])
def po():
 return jsonify({ "dirs": "a7aneeek"})


if __name__ == '__main__':
    app.run(port=80, debug=True)  # Use port 80