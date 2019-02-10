from pprint import pprint

import flask
from flask import jsonify, request, Request

from config import config


HOST = config['default']['host']
PORT = config['default']['port']

app = flask.Flask(__name__)

@app.route("/slack/userrequest", methods=["POST"])
def user_request():
    return handle_request(request)


def handle_request(request: Request):
    form = request.form
    print("content type", request.content_type)
    print("form", form)

    print(form["text"])

    return jsonify({"text": "ario is da best 😉"})

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)

