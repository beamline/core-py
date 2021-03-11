from abc import ABC, abstractmethod
import paho.mqtt.client as mqtt
from beamline.model.parameters import *


class AbstractMiner(ABC):

    def __init__(self, id):
        self._id = id
        self._name = ""
        self._description = ""
        self._running = False
        self._configured = True
        self._stream = Stream()
        self._client = mqtt.Client()

    @abstractmethod
    def configure(self, configuration):
        pass

    @abstractmethod
    def consume_event(self, case_id, activity_name):
        pass

    @abstractmethod
    def get_views(self, configuration):
        pass

    @abstractmethod
    def get_configuration_parameters(self):
        pass

    @abstractmethod
    def get_view_parameters(self):
        pass

    def stream(self, stream):
        self._stream = stream

    def on_message(self, client, userdata, msg):
        structure = msg.topic.split("/")
        activity_name = structure[-1]
        case_id = structure[-2]
        self.consume_event(case_id, activity_name)

    def start(self):
        if self._running :
            raise Exception("Miner instance already running")
        if not self._configured:
            raise Exception("Miner instance not yet configured")

        self._client.connect(self._stream.broker_host, 1883, 60)
        self._client.subscribe(self._stream.topic_base + "/" + self._stream.process_name + "/#")
        self._client.on_message = self.on_message

        self._client.loop_start()
        self._running = True

    def stop(self):
        if not self._running:
            raise Exception("Miner instance not running")
        self._client.disconnect()
        self._client.loop_stop()

    def serialize(self):
        return {
            "id": self._id,
            "name": self._name,
            "description": self._description,
            "configurationParameters": [
                x.serialize() for x in self.get_configuration_parameters()
            ],
            "viewParameters": [
                x.serialize() for x in self.get_view_parameters()
            ]
        }