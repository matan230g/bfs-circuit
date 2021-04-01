
class Gate:
    def __init__(self, txt):
        self.txt = txt
        txt = txt.replace('[', '')
        txt = txt.replace(']', '')
        temp = txt.split(',')
        self.type = temp[0]
        self.output=temp[1]

    def __str__(self):
         return "Name: {0}\tGenders: {1} Country: {2} ".format(self.type,self.output)
