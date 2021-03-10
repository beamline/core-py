from enum import Enum


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