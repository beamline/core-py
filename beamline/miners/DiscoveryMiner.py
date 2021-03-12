from beamline.miners.abstract import *
from beamline.model.parameters import *
from beamline.model.views import *
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
        config = ""
        for c in configuration:
            config += c.name + " = " + c.value + "<br>"

        google_views = []
        for v in MinerViewGoogleType:
            google_views.append(MinerViewGoogle(str(v) + " view", v,
                ["Year", "Sales", "Expenses", "Profit"],
                [
                    ["2014", 1000, 400, 209],
                    ["2015", 2000, 800, 203],
                    ["2016", 7000, 500, 206],
                    ["2017", 3000, 300, 204],
                    ["2018", 5000, 900, 201]
                ],
                {"title": "Company Performance", "subtitle": "Sales, Expenses, and Profit: 2014-2017"}))

        return [
            MinerViewRaw("Configuration", config),
            MinerViewRaw("Raw view", "Text example"),
            MinerViewBinary("Binary view", "http://speed.hetzner.de/100MB.bin"),
            MinerViewGraphviz("Graphviz view", "digraph G {A->B->D; A->C->D;}"),
        ] + google_views