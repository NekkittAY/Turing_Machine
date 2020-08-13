class Tape(object):
    blank = " "
    def __init__(self, tape_string = ""):
        self.tape = dict(enumerate(tape_string))
        
    def __str__(self):
        s = ""
        min_used_index = min(self.tape.keys()) 
        max_used_index = max(self.tape.keys())
        for i in range(min_used_index, max_used_index):
            s += self.tape[i]
        return s    
   
    def __getitem__(self,index):
        if index in self.tape:
            return self.tape[index]
        else:
            return Tape.blank

    def __setitem__(self, pos, char):
        self.tape[pos] = char
        
class TuringMachine(object):
    def __init__(self, tape = "", blank = " ", init_state = "", final = None, func = None):
        self.tape = Tape(tape)
        self.position = 0
        self.blank = blank 
        self.state = init_state
        if func == None:
            self.func = {}
        else:
            self.func = func
        if final == None:
            self.final = set()
        else:
            self.final = set(final)
            
    def get_tape(self):
        return str(self.tape)
        
    def step(self):
        char_position = self.tape[self.position]
        x = (self.state, char_position)
        if x in func:
            y = self.func[x]
            self.tape[self.position] = y[1]
            if y[2] == "L":
                self.position -= 1
            elif y[2] == "R":
                self.position += 1
            self.state = y[0]
            
    def final_tape(self):
        if self.state in self.final:
            return True
        else:
            return False
