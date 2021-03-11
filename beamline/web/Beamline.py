import flask
import copy
from flask import jsonify, request, make_response
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
    def get_miner_by_id(id):
        for m in Beamline.miners:
            if str(m._id) == id:
                return m
        return None

    @staticmethod
    def get_instance_by_id(id):
        for i in Beamline.instances:
            if str(i._id) == id:
                return i
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
    miner = Beamline.get_miner_by_id(minerid)
    if miner is None:
        return make_response("Missing miner", 404)
    miner_klass = miner.__class__
    miner_instance = MinerInstance(miner_klass(miner._id), configuration)
    Beamline.instances.append(miner_instance)
    return miner_instance.serialize()


@Beamline.app.route('/api/v1/instances/<instanceid>/start', methods=['GET'])
def instances_start(instanceid = None):
    instance = Beamline.get_instance_by_id(instanceid)
    if instance is None:
        return make_response("Missing instance", 404)
    instance.start()
    return "true"


@Beamline.app.route('/api/v1/instances/<instanceid>/stop', methods=['GET'])
def instances_stop(instanceid = None):
    instance = Beamline.get_instance_by_id(instanceid)
    if instance is None:
        return make_response("Missing instance", 404)
    instance.stop()
    return "true"


@Beamline.app.route('/api/v1/instances/<instanceid>/status', methods=['GET'])
def instances_status(instanceid = None):
    instance = Beamline.get_instance_by_id(instanceid)
    if instance is None:
        return make_response("Missing instance", 404)
    return instance.status


@Beamline.app.route('/api/v1/instances/<instanceid>/delete', methods=['DELETE'])
def instances_delete(instanceid = None):
    instance = Beamline.get_instance_by_id(instanceid)
    if instance is None:
        return make_response("Missing instance", 404)
    Beamline.instances.remove(instance)
    return instance.status