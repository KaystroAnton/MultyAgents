class Agent:
    def __init__(self, agent_id, agent_number=0,):
        self.agent_id = agent_id
        self.agent_number = agent_number
        self.connections = [self]
        self.info = []
    def get_agent_number(self):
        return self.agent_number

    def get_connections(self):  # get connections from near agent
        for j in self.connections:
            for i in j.connections:
                if not self.info.count([i, i.get_agent_number()]):
                    self.info.append([i, i.get_agent_number()])

    def add_connection(self, agent):  # add link between agents
        if not self.connections.count(agent):
            self.connections.append(agent)
        if not agent.connections.count(self):
            agent.connections.append(self)

    def update_info(self):  # updating agent memory
        for j in self.connections:
            for i in j.info:
                if not self.info.count(i):
                    self.info.append(i)

    def give_result(self):
        result = 0.0
        for i in self.info:
            result += i[1]
        return result/len(self.info)

