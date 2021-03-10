class Stream:
    def __init__(self, process_name, broker_host, topic_base):
        self.process_name = process_name
        self.broker_host = broker_host
        self.topic_base = topic_base