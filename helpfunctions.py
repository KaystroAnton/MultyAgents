from pair import Pair
from agentTask2 import Agent
from Constants import N,can_change,iterr

list_of_pairs = [[0,1],[1,2],[1,3],[2,4],[3,4],[4,5],[5,0],[3,2]] # with this list can create pairs
start_numbers = [5000,3500,2300,3150,7400,1100] # start agent numbers

def start_agents():
    agents = []
    for i in range(N): # innit list of agents
        agents.append(Agent(i,start_numbers[i]))
    return agents

def start_pairs(agents):
    for i in list_of_pairs: # add pairs to agents
        if i != list_of_pairs[can_change]:
            agents[i[0]].add_pair(Pair(agents[i[0]],agents[i[1]]))
        else: # set flag to pair that can disappear and add it to agent
            agents[i[0]].add_pair(Pair(agents[i[0]], agents[i[1]],True))

def main_loop(agents):
    for i in range(iterr): # count iterations
        for a in agents: # first step in the loop - all agents send messages to neighbours
            a.send_messages()
        for a in agents: # second step in the loop - all agents update their numbers according to protocol
            a.update_value()
        for c in range(N):
            print("agent number", c, "have number", agents[c].get_agent_number(), "in iter", i)
        print()



