import abc

class Transportation(metaclass = abc.ABCMeta):
    def __init__(self, s, e, d):
        self.start_place = s
        self.end_place = e
        self.distance = d
    def getstart(self):
        return self.start_place
    def getend(self):
        return self.end_place
    def getdistance(self):
        return self.distance
    @abc.abstractmethod
    def find_cost(self):
        pass

class walk(Transportation):
    def __init__(self, s, e, d):
        super().__init__(s, e, d)
    def find_cost(self):
        return 0

class taxi(Transportation):
    def __init__(self, s, e, d):
        super().__init__(s, e, d)
    def find_cost(self):
        return super().getdistance() * 40

class train(Transportation):
    def __init__(self, s, e, d, stop):
        super().__init__(s, e, d)
        self.stop = stop
    def find_cost(self):
        return self.stop * 5

me = [walk("KMITL","KMITL SCB Bank",0.6),
        taxi("KMITL SCB Bank","Ladkrabang Station",5),
        train("Ladkrabang Station","Payathai Station",40,6),
        taxi("Payathai Station","The British Council",3)]

for trans in me:
    print('Start:', trans.getstart(), 'End:', trans.getend(),'Distance:', trans.getdistance(),'Cost:', trans.find_cost())
