from enum import Enum


class Stream:
    def __init__(self, process_name, broker_host, topic_base):
        self.process_name = process_name
        self.broker_host = broker_host
        self.topic_base = topic_base

    @staticmethod
    def parse(json):
        process_name = json["processName"]
        broker_host = json["brokerHost"]
        topic_base = json["topicBase"]
        return Stream(process_name, broker_host, topic_base)

    def serialize(self):
        return {
            "processName": self.process_name,
            "brokerHost": self.broker_host,
            "topicBase": self.topic_base
        }


class MinerParameterType(str, Enum):
    STRING = "STRING"
    INTEGER = "INTEGER"
    DOUBLE = "DOUBLE"
    FILE = "FILE"
    RANGE_0_1 = "RANGE_0_1"
    CHOICE = "CHOICE"


class MinerParameter:
    def __init__(self, name = "", type = MinerParameterType.STRING, default_vlaue = ""):
        self.name = name
        self.type = type
        self.default_value = default_vlaue

    def serialize(self):
        return {
            "name": self.name,
            "type": self.type,
            "defaultValue": self.default_value
        }


class MinerParameterValue:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def serialize(self):
        return {
            "name": self.name,
            "value": self.value
        }


class MinerInstanceConfiguration:
    def __init__(self, name, stream):
        self.name = name
        self.stream = stream
        self.parameter_values = []

    @staticmethod
    def parse(json):
        name = json["name"]
        stream = Stream.parse(json["stream"])
        config = MinerInstanceConfiguration(name, stream)
        for c in json["parameterValues"]:
            config.parameter_values.append(MinerParameterValue(c["name"], c["value"]))
        return config

    def serialize(self):
        return {
            "name": self.name,
            "stream": self.stream.serialize(),
            "parameterValues": [x.serialize() for x in self.parameter_values]
        }
