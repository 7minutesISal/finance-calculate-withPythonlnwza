datainput = ["FV","I","N"]

def getinput(datainput):
    value = []
    for i in range(len(datainput)):
        dataReal = int(input(f"{i}"))
        value.append(dataReal)
    return value

class calculateFun :
    def __init__(self,FV,I,N):
        self.fv = FV
        self.i = I/100
        self.n = N

    def calculatePV(self):
        pv = self.fv * (1 / ((1 + self.i) ** self.n))
        return pv

FV,I,N = getinput("FV:","I:","N:")

PVdata = calculatefun(FV,I,N)
data = PVdata.calculatePV()
print(f"ได้เท่ากับ{data:.2f}")