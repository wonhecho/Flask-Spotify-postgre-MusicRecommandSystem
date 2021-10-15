from flask                      import Flask
from flask_restful              import Resource,Api,reqparse
from view                       import create_endpoints
from service.service            import BaseService
from model.model                import BaseDao
from view                       import create_endpoints
import psycopg2
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np

class Services:
	pass

def create_connection_pool():

    #Create Connection Pool
    pool = psycopg2.connect(
        host='localhost',
        dbname='test',
        user = 'postgres',
        password='root',
        port='5432'
    )

    #Return Connection Pool
    return pool

def create_pipline():
    data = pd.read_csv('./data.csv')
    data = data[data["popularity"]>50]
#    data = pd.read_csv('./testdata.csv')
    song_cluster_pipeline = Pipeline([('scaler', StandardScaler()), 
                                  ('kmeans', KMeans(n_clusters=20, 
                                   verbose=2, n_jobs=4))],verbose=True)

    X = data.select_dtypes(np.number)
    number_cols = list(X.columns)
    song_cluster_pipeline.fit(X)
    song_cluster_labels = song_cluster_pipeline.predict(X)
    data['cluster_label'] = song_cluster_labels
    return song_cluster_pipeline, data, number_cols
    


def create_app():

    app           = Flask(__name__, static_url_path='')
    api           = Api(app)
    app.config['JSON_AS_ASCII'] = False
    app.debug     = True

    database      = create_connection_pool()

    pipline, data, number_cols = create_pipline()

    base_model    = BaseDao(database)
    services = Services
    services.base_service   = BaseService(base_model,pipline,data,number_cols)
    create_endpoints(app,services)

    return app
