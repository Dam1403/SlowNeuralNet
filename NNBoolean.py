import ActFuncts
from NeuralNet import NeuralNet

def main():
    arr3d = [ [ [1,2],[3,4] ] ,[ [5,6],[7,8] ]  ]
    NN = NeuralNet(3,2,ActFuncts.sigmoid)
    NN.set_weights_arr(arr3d)
    print(NN)


main()
