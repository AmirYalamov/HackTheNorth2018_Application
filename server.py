import json
from time import time
import requests
from flask import Flask, jsonify, request

'''
@Author : Aman Adhav
@Description : Creating a webhook/api for REST Calls between the android keyboard
@Date : 2018-09-15
'''

class Analysis : 
    analyzed_sentence = "Testing"
    analyzed_place_interest = "Face book"


app = Flask(__name__)
@app.route('/api/message', methods=['POST'])
def message_recieve():
    message_recieved = request.get_json()
    print(message_recieved["message"])
    required = ['message','image','video'] #defines what are our 3 different platforms
    '''
    if not all(k in message_recieved for k in required):
        return "Missing values", 400    
    '''
    response = {'sentiment analysis' : (Analysis.analyzed_sentence),
                'place interest' : (Analysis.analyzed_place_interest),
                }
    return jsonify(response), 200

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int,help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(host="0.0.0.0", port = port)