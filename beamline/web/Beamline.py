import flask
from beamline.web.controllers import *
from flask import jsonify
from flask_cors import CORS


class Beamline:
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True
    CORS(app)

    def serve(self):
        Beamline.app.run()


@Beamline.app.route('/api/v1/miners', methods=['GET'])
def miners():
    return jsonify(MinerController.miners)
