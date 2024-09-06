import numpy

class neuralNetwork:
    
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # set number of nodes in each input, hidden, output layer
        self.innodes = inputnodes
        self.hnodes = hiddennodes
        self. onnodes = outputnodes
        
        # learning rate
        self.lr = learningrate
        pass
    
    def train():
        pass
    
    def query():
        pass
    
    
# number of input, hidden and output nodes
input_nodes = 3
hidden_nodes = 3
output_nodes = 3

# learning rate is 0.3
learning_rate = 0.4

# create instance of neural network
n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)