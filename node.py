class Node:
    def __init__(self, name):
        self.name = name
        # self.value = name # temp - delete later
        if name.find("-") != -1:
            self.value = 0
        else:
            self.value = 1

    def set_value(self, value):
        self.value = value

    def __str__(self):
        # return " node: " + self.name + " value: " + ("0" if self.value is None else str(self.value))
        return " node: " + self.name + " value: " + str(self.value)
