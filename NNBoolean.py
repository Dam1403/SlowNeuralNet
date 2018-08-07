import ActFuncts
from NeuralNet import NeuralNet

def main():
    arr3d = [ [.9,.3,.4],\
              [.2,.8,.2],\
              [.1,.5,.6]]


    NNinput = [.9,.1,.8]
    NN = NeuralNet(2,2,ActFuncts.sigmoid)
    NN.set_weights_arr(arr3d)

    print(NNinput)
    print(NN)
    print("Eval Result: " + str(NN.evaluate(NNinput)))


main()
