import random
from pair import noise
from Constants import alpha
class Agent:
    def __init__(self, agent_id, agent_number=0):
        self.agent_id = agent_id
        self.pairs = []
        self.agent_number = agent_number
        self.buffer = []
    def get_agent_number(self):
        return self.agent_number

    def add_pair(self, pair):  # add info about which agent can receive message from this agent
        if not self.pairs.count(pair):
            self.pairs.append(pair)

    def send_messages(self):  # send messages to all available agents
        for j in self.pairs:
            j.send_message(self.agent_number)

    def add_buffer(self,value):
        self.buffer.append(value)

    def update_value(self): # updating agent_number following local voting protocol
        if len(self.buffer) != 0:
            s = 0
            for i in self.buffer:
                s += (i - self.agent_number - noise())
            self.agent_number += alpha*s + random.normalvariate(mu = 0, sigma = 1)
        self.buffer = [] #clean buffer