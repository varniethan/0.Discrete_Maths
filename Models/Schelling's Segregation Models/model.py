# %matplotlib inline - #ONLY FOR JUPITER: A Magic function - plotting commands is displayed inline, where arguments are passed without parenthese or quotes.
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (11,5)  #set default figure size
from random import uniform, seed
from math import sqrt

seed(10)
class Agent:
    def __init__(self, type):
        self.type = type
        self.draw_location()

    def draw_location(self):
        self.location = uniform(0,1), uniform(0,1)

    def get_distance(self, other):
        a = (self.location[0] - other.location[0])
        b = (self.location[1] - other.location[1])
        return sqrt(a + b)

    def happy(self, agents):
        "TRUE if the half or 10 nearest neighbours are of the same colour"
        "Distances are 2D list (distance, agent) and the distance is from the agent to the self"
        distances = []
        for agent in agents:
            if self != agent:
                distance = self.get_distance(agent)
                distances.append(distance, agent)
        distances.sort()
        # == Extract the neighboring agents == #
        neighbors = [agent for d, agent in distances[:num_neighbours]]
        # == Count how many neighbors have the same type as self == #
        num_same_type = sum(self.type == agent.type for agent in neighbors)
        return num_same_type >= require_same_type

    def update(self, agents):
        while not self.happy(agents):
            self.draw_location()

def plot_distribution(agents, cycle_num):
    "Plot the distribution of agents after cycle_num rounds of the loop."
    x_values_0, y_values_0 = [], []
    x_values_1, y_values_1   = [], []
    #Location of each type is obtained
    for agent in agents:
        X, Y = agent.location
        if agent.type == 0:
            x_values_0.append(X)
            y_values_0.append(Y)
        else:
            x_values_1.append(X)
            x_values_1.append(Y)
        fig, ax = plt.subplots(figsize=(8, 8))
        plot_args = {'markersize': 8, 'alpha': 0.6}
        ax.set_facecolor('azure')
        ax.plot(x_values_0, y_values_0, 'o', markerfacecolor='orange', **plot_args)
        ax.plot(x_values_1, y_values_1, 'o', markerfacecolor='green', **plot_args)
        ax.set_title(f'Cycle {cycle_num - 1}')
        plt.show()




# == Main == # - Define the constants
num_of_type_0 = 250
num_of_type_1 = 250
num_neighbours = 10
require_same_type = 5

# == Create a list of agents == #
agents = [Agent(0) for i in range(num_of_type_0)]
agents.extend([Agent(1) for i in range(num_of_type_1)])

count = 1
# ==  Loop until none wishes to move == #
while True:
    print("Entering a loop", count)
    plot_distribution(agents, count)
    count += 1
    no_one_moved = True
    for agent in agents:
        old_location = agent.location
        agent.update(agents)
        if agent.location != old_location:
            no_one_moved = False
    if no_one_moved:
        break

# ==  Conclusion - THE END == #
print("Thanks for using our wonderful simulator. The program is Convered and terminating successfully")
