import uuid


class MinerInstance:

    def __init__(self, miner, configuration):
        self._id = uuid.uuid1()
        self._miner = miner
        self.status = "not_mining"
        self._configuration = configuration

        self.configuring()
        miner.stream(configuration.stream)
        miner.configure(configuration)
        self.status = "not_mining"

    def start(self):
        self.status = "mining"
        self._miner.start()

    def stop(self):
        self.status = "not_mining"
        self._miner.stop()

    def configuring(self):
        self.status = "configuring"

    def serialize(self):
        return {
            "id": self._id,
            "miner": self._miner.serialize(),
            "configuration": self._configuration.serialize()
        }