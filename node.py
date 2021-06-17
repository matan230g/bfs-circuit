from sympy import symbols
class Node:
    def __init__(self, name):
        self.name = name
        if name.find("-")!= -1:
            self.value = False
        else:
            self.value = True
        temp = self.name
        temp = str(temp).replace('-', "")
        self.symbol = symbols(temp)

    def calculate_value(self, name):
        if name.find("-") != -1:
            self.value = False
        else:
            self.value = True

    def set_value(self, value):
        self.value = value

    def get_name(self):
        temp = self.name
        temp = str(temp).replace('-',"")
        return temp

    def __str__(self):
        return " node: " + self.name + " value: " + str(self.value)
