import ActFuncts
from NeuralNet import NeuralNet

def main():
    NN = NeuralNet(3,3,ActFuncts.sigmoid)
    print(NN)


main()
