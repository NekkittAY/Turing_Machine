from turing_machine import TuringMachine
init_state = "init",
acecept = ["final"],
func = {("init", "0"):("init", "1", "R"),
        ("init", "1"):("init", "0", "R"),
        ("init", " "):("final"," ", "N")
        }
final = {"final"}

t = TuringMachine("101", 
                  init_state = "init",
                  final = final,
                  func = func)
                  
print("Input on Tape:\n" + t.get_tape())
while not t.final_tape():
    t.step()
print("Result of the Turing machine calculation:\n" + t.get_tape()) 
