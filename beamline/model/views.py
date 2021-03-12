from abc import ABC
from enum import Enum


class MinerViewType(str, Enum):
    RAW = "RAW"
    GRAPHVIZ = "GRAPHVIZ"
    BINARY = "BINARY"
    GOOGLE = "GOOGLE"


class MinerView(ABC):
    def __init__(self):
        self._name
        self._type
        self._value

    def serialize(self):
        return {
            "name": self._name,
            "type": self._type,
            "value": self._value
        }


class MinerViewRaw(MinerView):
    def __init__(self, name, value):
        self._name = name
        self._value = value
        self._type = MinerViewType.RAW


class MinerViewBinary(MinerView):
    def __init__(self, name, url):
        self._name = name
        self._value = url
        self._type = MinerViewType.BINARY


class MinerViewGraphviz(MinerView):
    def __init__(self, name, graphviz):
        self._name = name
        self._value = graphviz
        self._type = MinerViewType.GRAPHVIZ


class MinerViewGoogleType(str, Enum):
    SCATTER_CHART = "ScatterChart"
    AREA_CHART = "AreaChart"
    BAR_CHART = "BarChart"
    BUBBLE_CHART = "BubbleChart"
    COLUMN_CHART = "ColumnChart"
    PIE_CHART = "PieChart"
    HISTOGRAM = "Histogram"
    LINE_CHART = "LineChart"
    TABLE = "Table"


class MinerViewGoogle(MinerView):
    def __init__(self, name, type, headers, values, options):
        self._name = name
        self._type = MinerViewType.GOOGLE
        self._value = {
            "type": type,
            "data": [headers] + values,
            "options": options
        }