from flask import Flask, render_template
from flask_pymongo import PyMongo

import socket
import html
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://<usuario>:<senha>@<cluster>.mongodb.net/mapuche_dic"

mongo = PyMongo(app)
db = mongo.db

@app.route('/palabras', methods=['GET'])
def get_palabras():
    palabras = db.diccMAP_20230129_V01.find()
    return render_template('index.html',palabras=palabras)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
