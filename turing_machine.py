class Turing_Machine:
    def __init__(self,sTape,sPos,rules):
        self.sTape = sTape
        self.sPos = sPos
        self.rules = rules

    def tape(self):
        self.blank = ["#"]
        self.Tape = self.blank+self.sTape+self.blank

    def Machine(self):
        self.endTape = self.Tape
        if not(self.Tape[self.sPos]=="#"):
            pos = self.sPos
        else:
            pos = self.sPos+1
        while not(self.Tape[pos]=="#"):
            elem = self.Tape[pos]
            self.endTape[pos] = self.rules[elem][0]
            if self.rules[elem][1] == "L":
                pos-=1
            elif self.rules[elem][1] == "R":
                pos+=1
            else:
                print(self.endTape)
                break
            print(self.endTape)
