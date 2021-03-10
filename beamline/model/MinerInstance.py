import uuid


class MinerInstance:

    def __init__(self, miner, configuration):
        self._id = str(uuid.uuid1())
        self._miner = miner
        self._configuration = configuration