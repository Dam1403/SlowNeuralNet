class NeuralNet:



    def __init__(self, layer_count, layer_depth,activation_function):
        layer_count = layer_count + 2
        #plus 2 for input and output layers

        self.input_length = layer_depth
        self.layers = [];

        for i in range(0,layer_count):
            layer = []
            for j in range(0,layer_depth):
                layer += Neuron()
            self.layers += layer
        self.rel_table = RelationTable(layer_count,layer_depth)




    def set_weights(self,low_bound,high_bound):
        self.rel_table.init_weights(low_bound,high_bound)

        
    def evaulate(self, input_arr):
        self.layers[0] = input_arr.copy()

        for layer_index in range(0,layer_count - 1):
            self.IOcrunch_layer(layer_index)
        return layers[-1].copy()


    def IOcrunch_layer(self, layer_index):
        in_layer = self.layers[layer_index]
        out_layer = self.layers[layer_index + 1]
        weight = 0;

        for out_neuron_index in range(input_length):
            out_neuron = out_layer[out_neuron_index]
            new_value = 0
            for in_neuron_index in range(input_length):
                in_neuron = in_layer[in_neuron_index]
                weight = rel_get(layer_index,in_neuron_index,out_neuron_index)
                new_value += in_neuron.act_funct(in_neuron.value * weight)
            out_neuron.value = new_value



class NNInputLengthException(Exception):
    pass


class NNLayerLengthException(Exception):
    pass
