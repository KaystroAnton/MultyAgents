import random
from agentTask1 import Agent
N = 6  # number of agents
isEnd = False

agents = [Agent(i,random.randint(-100,100)) for i in range(N)] # massive of agents
numbers = [agents[i].agent_number for i in range(N)]
avgTrue = sum(numbers)/N
print(numbers, avgTrue)  # avg for check


# create connections
chain = [[i,i+1] for i in range(N-1)]
closed_circuit = [[i,i+1] for i in range(N-1)]
closed_circuit.append([N-1,0])
connection = chain
for link in connection:
    agents[link[0]].add_connection(agents[link[1]])


# on start every agent get info from neighbors
for i in agents:
    i.get_connections()


# main loop
for simulation_step in range(N-2):  # simulation step
    if isEnd:
        break
    for i in range(N):  # in each step we work with every agent
        if len(agents[i].info) == 6:
            print("on step", simulation_step, "algorithm ends work wih result", agents[i].give_result())
            isEnd = True
            break
        agents[i].update_info()
