class Observation:
    def __init__(self, observation):
        li = observation.split(',', 2)
        self.number = li[1]
        li[2] = li[2].replace('[', '')
        li[2] = li[2].replace(']', '')
        self.inputs_outputs = li[2].split(',')
        self.inputs = []
        self.output = []
