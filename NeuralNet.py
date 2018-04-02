from Neuron import Neuron
from RelationTable import RelationTable
class NeuralNet:
#if you can get solve weight = deltaO  you can piecewise node functs within threads
    def __init__(self, layer_count, layer_depth,activation_function):
        self.true_layer_count = layer_count
        self.layer_count = layer_count
        self.weight_layer_count = layer_count - 1


        #plus 2 for input and output layers
        self.input_length = layer_depth
        self.layers = [];
        for i in range(0,self.layer_count):
            layer = []
            for j in range(0,layer_depth):
                layer.append(Neuron(activation_function))
            self.layers.append(layer)
        print(self.layers)
        self.rel_table = RelationTable(self.layer_count,layer_depth)


    def __str__(self):
        result = ""
        result += "LayerCount: " + str(self.layer_count) + "\n"
        result += "LayerDepth: " + str(self.input_length) + "\n"
        result += "Weights: \n\n" + str(self.rel_table)
        return result



    #[layer_index][in_neuron_index][out_nueron_index]
    def set_weights_rand(self,low_bound,high_bound):
        self.rel_table.init_weights(low_bound,high_bound)
    def set_weights_arr(self,arr3d):
        # +2(IO layers) -1(WeightLayers) error check better
        if(len(arr3d) != self.weight_layer_count):
            raise NNWeightLayerException("Weight Array Layer Count Mismatch")
        if(len(arr3d[0][0]) != self.input_length):
            raise NNWeightDepthException("Weight Array Layer Depth Mismatch")

        for layer_index in range(0,len(arr3d)):
            for in_neuron_index in range(0,len(arr3d[0][0])):
                for out_nueron_index in range(0,len(arr3d[0][0])):
                    value = arr3d[layer_index][in_neuron_index][out_nueron_index]
                    self.rel_table.rel_set(layer_index,in_neuron_index,out_nueron_index,value)


    def set_weights_file(self,filename):
        with open(filename,"r") as f:
            line = f.readline()
            while line.strip() != "":
                line = line.strip()
                linearr = line.split(" ")

    def evaluate(self, input_arr):
        self.input_layer_write(input_arr)
        for layer_index in range(0,self.weight_layer_count):
            self.IOcrunch_layer(layer_index)
        return [self.layers[-1][i].value for i in range(0,self.input_length)]



    def IOcrunch_layer(self, layer_index):
        print("Layer_index "+str(layer_index))
        in_layer = self.layers[layer_index]
        out_layer = self.layers[layer_index + 1]
        weight = 0;

        for out_neuron_index in range(self.input_length):
            out_neuron = out_layer[out_neuron_index]
            new_value = 0
            for in_neuron_index in range(self.input_length):
                in_neuron = in_layer[in_neuron_index]
                weight = self.rel_table.rel_get(layer_index,in_neuron_index,out_neuron_index)
            new_value += in_neuron.act_funct(in_neuron.value * weight)
            out_neuron.value = new_value


    def input_layer_write(self,input_arr):
        #error check
        in_layer = self.layers[0]
        for i in range(0,self.input_length):
            in_layer[i].value = input_arr[i]




def strs_cast_floats(str_arr):
    for i in range(0,len(str_arr)):
        str_arr[i] = float(i)
    return str_arr



class NNInputLengthException(Exception):
    pass

class NNLayerLengthException(Exception):
    pass

class NNWeightLayerException(Exception):
    pass

class NNWeightDepthException(Exception):
    pass
