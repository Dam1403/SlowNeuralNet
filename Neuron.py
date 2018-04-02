class Neuron:

    def __init__(self,activation_function):
        self.value = 0
        self.act_funct = activation_function

    def __str__(self):
        return "Neuron: " + str(self.value) + " Afunction: " + self.act_funct.__name__
