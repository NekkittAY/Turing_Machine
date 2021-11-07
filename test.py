from Turing_Machine import Turing_Machine

start = list(input().split()) # 0 1 1 0 1
position = int(input()) # 0
rules = {"0":"1R","1":"0R"}
TM = Turing_Machine(start,position,rules)
TM.tape()
TM.Machine()
