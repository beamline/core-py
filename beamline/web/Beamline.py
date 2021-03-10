import flask
from flask import request, jsonify
from beamline.controller import MinerController


class Beamline:
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True

    def serve(self):
        Beamline.app.run()


@Beamline.app.route('/api/v1/miners', methods=['GET'])
def miners():
    return jsonify(MinerController.MinerController.miners)
