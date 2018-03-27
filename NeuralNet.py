class NeuralNet:



    def __init__(self, layer_count, layer_depth):
        self.layers = [];
        for i in range(0,layer_count):
            layer = []
            for j in range(0,layer_depth):
                layer += Neuron()
            self.layers += layer

        self.rel_dict = {}
        for i in range(0,layer_depth):
