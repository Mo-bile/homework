from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://mo:jae@cluster0.joa3ijk.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta
@app.route('/')
def home():
   return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    nick_receive = request.form['nick_give']
    reple_receive = request.form['reple_give']

    doc = {
        'nick': nick_receive,
        'reple': reple_receive
    }
    db.kkk.insert_one(doc)

    return jsonify({'msg':'POST 연결 완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    reple_list = list(db.kkk.find({}, {'_id': False}))
    print(reple_list)
    return jsonify({'reple':reple_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5001, debug=True)