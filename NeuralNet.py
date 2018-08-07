from Neuron import Neuron
from RelationTable import RelationTable
import numpy
class NeuralNet:
#if you can get solve weight = deltaO  you can piecewise node functs within threads
    def __init__(self, layer_count, layer_depth,activation_function):
        self.layer_count = layer_count
        self.layer_depth = layer_depth
        self.net = numpy.random.rand(layer_count,layer_depth)
        self.activation_function = activation_function
        self.curr_hout = []
		


    def __str__(self):
        result = ""
        result += "LayerCount: " + str(self.layer_count) + "\n"
        result += "LayerDepth: " + str(self.layer_depth) + "\n"
        result += "Weights: \n\n" + str(self.net)
        return result

    def prep_train(self,learning_rate):
        self.learning_rate = learning_rate


    def set_weights_arr(self,arr2d):
        self.net = numpy.array(arr2d)
        self.layer_count = self.net.shape[1]
        self.layer_depth = self.net.shape[0]


    def set_weights_file(self,filename):
        with open(filename,"r") as f:
            line = f.readline()
            while line.strip() != "":
                line = line.strip()
                linearr = line.split(" ")

    def evaluate(self, input_arr):
        input_arr = numpy.array(input_arr)
        hin = numpy.dot(self.net, input_arr)
        hout = self.activation_function(hin)
        print("hout: 0" + str(hout))
        for layer_index in range(1,self.layer_count - 1):
            hin = numpy.dot(self.net,hout)
            hout =  self.activation_function(hin)
            print("hout: {0} ".format(layer_index) + str(hout))
        return hout


    def IOcrunch_layer(self, layer_index):
        pass


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
