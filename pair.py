import random
from Constants import crash_chance,delay_chance, delayMin, delayMax, mu, std_dev

def noise():
    while True:
        noises = random.normalvariate(mu = mu, sigma = std_dev)
        if -500 <= noises <= 500:
            break
    return noises

class Pair:
    def __init__(self, agent_send, agent_receive, flag =False): # constructor
        self.agent_send = agent_send
        self.agent_receive = agent_receive
        self.flag = flag
        self.buffer = []

    def send_message(self, value):  # sending message from agent_id_send to agent_id_receive
        if random.random() > 1 - crash_chance and self.flag: # check if connection lose
            pass
        else:
            if random.random() > 1 - delay_chance:  # add message to buffer with random delay
                self.buffer.append([value,random.randrange(start = delayMin,stop = delayMax)])
            else: # add message to buffer with no delay
                self.buffer.append([value, 1])
        print(self.buffer)
        for i in self.buffer: #delay decreases for all messages in buffer
            if i[1] != 0:
                i[1] -= 1
            if i[1] == 0: # if delay = 0, send message with noises to agent_receive and delete message from buffer
                self.agent_receive.add_buffer(i[0] + noise())
                self.buffer.remove(i)
