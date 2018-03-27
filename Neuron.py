class Neuron:

    def __init__(self,activation_function):
        self.value = 0
        self.act_funct = activation_function

    def __str__(self):
        return "Neuron: " + self.value + " Afunction: " + self.activation_function.__name__
