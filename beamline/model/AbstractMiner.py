from abc import ABC
import paho.mqtt.client as mqtt
import uuid
import json


class AbstractMiner(ABC):

    def __init__(self):
        self._id = uuid.uuid1()
        self._name = ""
        self._running = False
        self._configured = True
        self._miner_instance
        self._stream
        self._client = mqtt.Client()

    def configure(self, configuration):
        pass

    def consume_event(self, case_id, activity_name):
        pass

    def get_views(self, configuration):
        pass

    def get_configuration_parameters(self):
        pass

    def get_view_parameters(self):
        pass

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
        return {"aaa":12}  #json.dumps(self, default=lambda o: o.__dict__)