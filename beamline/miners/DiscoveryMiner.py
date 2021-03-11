from beamline.miners.abstract import *
from beamline.model.parameters import *
import uuid


class DiscoveryMiner(AbstractMiner):

    def __init__(self, id=uuid.uuid1()):
        super(DiscoveryMiner, self).__init__(id)
        self._name = "Discovery Miner"
        self._description = ""

        self.para_test1 = ""
        self.para_test2 = ""

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

    def configure(self, configuration):
        self.para_test1 = configuration.get("test1").value
        self.para_test2 = configuration.get("test2").value

    def consume_event(self, case_id, activity_name):
        print(case_id + " -- " + activity_name + " -- " + self.para_test1 + "," + self.para_test2)

    def get_views(self, configuration):
        pass