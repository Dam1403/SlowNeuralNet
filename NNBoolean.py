import ActFuncts
from NeuralNet import NeuralNet

def main():
    layer1 = [ [.9,.3,.4],
              [.2,.8,.2],
              [.1,.5,.6]]

    layer2 = [ [.3,.7,.5],
              [.6,.5,.2],
              [.8,.1,.9]]


    NNinput = [.9,.1,.8]
    NN = NeuralNet(3,3,ActFuncts.sigmoid)
    NN.set_weight_layers(layer1,layer2)

    print(NNinput)
    print(NN)
    print("Eval Result: " + str(NN.evaluate(NNinput)))


main()
