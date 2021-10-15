import os
import requests
from flask          import request, jsonify
from flask_restful import Resource,Api
from werkzeug.utils import secure_filename

def create_endpoints(app, services):
    base_service = services.base_service
    @app.route("/Create_user_table", methods = ['GET', 'POST'])
    def base():
        result = base_service.createTable()
        return result
    @app.route("/Insert_Dummy_Data", methods = ['GET', 'POST'])
    def insert():
        result = base_service.InsertData()
        return result
    @app.route("/Recommand_Data", methods = ['GET', 'POST'])
    def Recommand():
        result = base_service.RecommandSong()
        return result