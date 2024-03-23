from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from CNN_Classifier.utils.common import decodeImage
from CNN_Classifier.pipeline.predict import *