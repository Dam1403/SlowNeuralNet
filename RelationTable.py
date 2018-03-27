import random

class RelationTable:

    def __init__(self,layer_count,layer_depth):
        self.rel_arr = []
        self.layer_count = layer_count
        self.layer_depth = layer_depth
        layer_range = [i for i in range(0,layer_depth)]
        for layer_index in range(0,layer_count):
            rel_arr += [[0 for i in layer_range] for j in layer_range]

    def __str__(self):
        result = ""
        for layer_index in range(0, layer_count):
            result += "Layer " + str(layer_index) + ":\n\n"
            result += arr2arr2d_to_str(self.rel_arr[layer_index])
            result += "\n"
        return result

    def init_weights(self,low_bound,high_bound):
        for layer_index in range(0,layer_count):
            for in_neuron_index in range(0,layer_depth):
                for out_neuron_index in range(0,layer_depth):
                    self.rel_arr[layer_index][in_neuron_index][out_nueron_index]\
                     = random.uniform(low_bound,high_bound)

    def rel_get(self,layer_index,in_neuron_index,out_nueron_index):
        return self.rel_arr[layer_index][in_neuron_index][out_nueron_index]

    def rel_set(self,layer_index,in_neuron_index,out_nueron_index,rel_value):
        self.rel_arr[layer_index][in_neuron_index][out_nueron_index] = rel_value


def arr2d_to_str(arr2d):
    result = ""
    for i in range(0,len(arr2d)):
        result += "| "
        for j in range(0,len(arr2d[i])):
            result += str(round(arr2d[i][j],2)) + " "
        result += "|\n"
    return result
