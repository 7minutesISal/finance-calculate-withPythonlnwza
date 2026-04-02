

class calculateFun :
    def __init__(self,FV,I,N):
        self.fv = FV
        self.i = I/100
        self.n = N

    def calculatePV(self):
        pv = self.fv * (1 / ((1 + self.i) ** self.n))
        return pv

PVdata = calculatefun(FV,I,N)
data = PVdata.calculatePV()
print(f"ได้เท่ากับ{data:.2f}")