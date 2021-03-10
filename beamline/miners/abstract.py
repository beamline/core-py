from abc import ABC
import paho.mqtt.client as mqtt
import uuid


class AbstractMiner(ABC):

    def __init__(self):
        self.id = uuid.uuid1()
        self._name = ""
        self._description = ""
        self._running = False
        self._configured = True
        # self._miner_instance
        # self._stream
        self._client = mqtt.Client()

    def configure(self, configuration):
        raise NotImplemented

    def consume_event(self, case_id, activity_name):
        raise NotImplemented

    def get_views(self, configuration):
        raise NotImplemented

    def get_configuration_parameters(self):
        raise NotImplemented

    def get_view_parameters(self):
        raise NotImplemented

    def on_message(self, userdata, msg):
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

        self._client.loop_forever()
        self._running = True

    def stop(self):
        if not self._running:
            raise Exception("Miner instance not running")
        self._client.disconnect()

    def serialize(self):
        return {
            "id": self.id,
            "name": self._name,
            "description": self._description,
            "configurationParameters": [
                x.serialize() for x in self.get_configuration_parameters()
            ],
            "viewParameters": [
                x.serialize() for x in self.get_view_parameters()
            ]
        }