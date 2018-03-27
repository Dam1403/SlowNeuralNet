

class RelationTable:

    def __init__(self,layer_count,layer_depth):
        self.rel_arr = []
        layer_range = [i for i in range(0,layer_depth)]
        for layer_index in range(0,layer_count):
            rel_arr += [[0 for i in layer_range for j in layer_range]


    def rel_get(layer_index,in_neuron_index,out_nueron_index):
        return rel_arr[layer_index][in_neuron_index][out_nueron_index]

    def rel_set(layer_index,in_neuron_index,out_nueron_index,rel_value):
        rel_arr[layer_index][in_neuron_index][out_nueron_index] = rel_value
