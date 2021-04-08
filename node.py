class Node:
    def __init__(self, name):
        self.name = name
        if name.find("-")  != -1:
            self.value = False
        else:
            self.value = True

    def calculate_value(self, name):
        if name.find("-") != -1:
            self.value = False
        else:
            self.value = True

    def set_value(self, value):
        self.value = value


    def __str__(self):
        return " node: " + self.name + " value: " + str(self.value)
