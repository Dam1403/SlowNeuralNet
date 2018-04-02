import ActFuncts
from NeuralNet import NeuralNet

def main():
    arr3d = [ [ [.1,.3],\
                [.2,.4] ]  ]

                
    NNinput = [.2,.8]
    NN = NeuralNet(2,2,ActFuncts.sigmoid)
    NN.set_weights_arr(arr3d)


    print(NN)
    print("Eval Result: " + str(NN.evaluate(NNinput)))



main()
