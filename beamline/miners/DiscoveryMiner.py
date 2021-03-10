from beamline.model.AbstractMiner import AbstractMiner
from beamline.model.MinerParameter import *


class DiscoveryMiner(AbstractMiner):

    def __init__(self):
        super(DiscoveryMiner, self).__init__()
        self._name = "Discovery Miner"
        self._description = ""

    def get_configuration_parameters(self):
        return [
            MinerParameter("test1", MinerParameterType.STRING, "test default value"),
            MinerParameter("test2", MinerParameterType.DOUBLE, "3.14"),
        ]

    def get_view_parameters(self):
        return [
            MinerParameter("test_view_1", MinerParameterType.STRING, "test default value"),
            MinerParameter("test_view_2", MinerParameterType.DOUBLE, "3.14"),
        ]