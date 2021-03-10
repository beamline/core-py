import uuid
from flask import jsonify


class MinerInstance:

    def __init__(self, miner, configuration):
        self._id = uuid.uuid1()
        self._miner = miner
        self._configuration = configuration

    def serialize(self):
        return {
            "id": self._id,
            "miner": self._miner.serialize(),
            "configuration": self._configuration.serialize()
        }