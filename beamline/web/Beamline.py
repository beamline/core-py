import flask
from flask import jsonify
from flask import request
from flask_cors import CORS

from beamline.model.instances import *
from beamline.model.parameters import *


class Beamline:
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True
    CORS(app)

    miners = []
    instances = []

    @staticmethod
    def get_by_id(id):
        for m in Beamline.miners:
            if str(m.id) == id:
                return m
        return None

    def serve(self):
        Beamline.app.run()


@Beamline.app.route('/api/v1/miners', methods=['GET'])
def get_miners():
    return jsonify([m.serialize() for m in Beamline.miners])


@Beamline.app.route('/api/v1/instances', methods=['GET'])
def get_instances():
    return jsonify([i.serialize() for i in Beamline.instances])


@Beamline.app.route('/api/v1/instances/<minerid>', methods=['POST'])
def instances_create(minerid = None):
    configuration = MinerInstanceConfiguration.parse(request.get_json())
    miner = Beamline.get_by_id(minerid)
    miner_instance = MinerInstance(miner, configuration)
    Beamline.instances.append(miner_instance)
    return miner_instance.serialize()