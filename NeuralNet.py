class NeuralNet:



    def __init__(self, layer_count, layer_depth):
        self.input_length = layer_depth
        self.layers = [];
        #plus 2 for input and output layers
        for i in range(0,layer_count + 2):
            layer = []
            for j in range(0,layer_depth):
                layer += Neuron()
            self.layers += layer
        self.rel_table = RelationTable(layer_count,layer_depth)

    def get_output(input_arr):
        if(len(input_arr) != self.input_length))
        {
            raise NNInputLengthException("Input array length doesn't match layer depth")
        }

    def IOcrunch_layer(layer_index):
        in_layer = layers[layer_index]
        out_layer = layers[layer_index + 1]


        for out_neuron_index in range(input_length):
            out_neuron = out_layer[out_neuron_index]
            for in_neuron_index in range(input_length):
                in_neuron = in_layer[in_neuron_index]
                





class NNInputLengthException(Exception):
    pass


class NNLayerLengthException(Exception):
    pass
