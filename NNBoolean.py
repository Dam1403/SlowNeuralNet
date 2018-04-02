import ActFuncts
from NeuralNet import NeuralNet

def main():
    arr3d = [ [ [.1,.3],[.5,.7] ]  ]
    NNinput = [.8,.2]
    NN = NeuralNet(2,2,ActFuncts.sigmoid)
    NN.set_weights_arr(arr3d)


    print(NN)
    print("Eval Result: " + str(NN.evaluate(NNinput)))



main()
