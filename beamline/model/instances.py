import uuid


class MinerInstanceConfiguration:
    def __init__(self, name, stream):
        self.name = name
        self.stream = stream
        self.parameter_values = []

    def serialize(self):
        return {
            "name": self.name,
            "stream": self.stream.serialize(),
            "parameterValues": [x.serialize() for x in self.parameter_values]
        }


class MinerInstance:

    def __init__(self, miner, configuration):
        self._id = uuid.uuid1()
        self._miner = miner
        self._configuration = configuration

    def serialize(self):
        return {
            "id": id,
            "miner": self._miner.serialize(),
            "configuration": self._configuration.serialize()
        }