
import requests
import json
import pymongo
from pymongo import MongoClient
import urllib.parse

username = "SamAshton"
password = "Grengo12"

conn = MongoClient("mongodb+srv://" + username + ":" + password + "@gym-music-cluster-619sw.mongodb.net/?authMechanism=SCRAM-SHA-1&authSource=Admin")
db = conn['gym_music']
collection = db['spotify']


audio_analysis_url = 'https://api.spotify.com/v1/audio-analysis/72aCha2Meq7txnk451hz7k'
access_token = 'BQAPOeVu58yMTOmoRpicBEa4jI13ImIJnyC8Zh_aCZlrz92YxBkwVMysJ5C7Vj3dwZTNxDUvRJcXkMyNnYGlkDGvrpPoXsReH3bjgQRh1rSUml-Ds3xbkCi2ICnSQ1WKDp_IK8fwf_7EJnXPZmmVcEUndFF9OQ'
headers = {
    'Content-Type':'application/json',
    'Authorization': 'Bearer BQCqORMalLwv_pUvfuarAilfqsluSaffYOMcZ6sPpJvgfsu7ae8jvR-JNyOp7wmDiSgpIZMnFi4NshLcJzLYVXiuuSXP_3cet318-WVojuDSeeUNF9yV3za8FqTJIA1ETgenS3rZPIx68cINm8tVdAH1gz8WMA'
}

params = {

}

response = requests.get(audio_analysis_url, params=params, headers=headers)
mydict = { "name": "John", "address": "Highway 37" }
collection.insert_one(mydict)