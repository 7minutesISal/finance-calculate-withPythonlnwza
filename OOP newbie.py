
MYlist = []
import math

class calculateFun :
    def __init__(self,FV=0,PV=0,PMT=0,I=0,N=0):
        self.fv = FV
        self.pv = PV
        self.pmt = PMT
        self.i = I/100
        self.n = N

    def calculatePV(self):
        pv = self.fv * (1 / ((1 + self.i) ** self.n))
        return pv

    def calculateFV(self):
        fv = self.pv * ((1+self.i)**self.n)
        return fv
    
class calculatePMT(calculateFun):
    def calculateFVlastByPMT(self):
        FVAl = self.pmt * ((((1+self.i)**self.n) - 1) / self.i)
        return FVAl
    
    def findFVfirstByPMT(self):
        FVAf = self.calculateFVlastByPMT()
        return FVAf * (1+self.i)
    
    def findPVlastByPMT(self):
        PVAl = self.pmt * ((1 - (1 / ((1+self.i)**self.n))) / self.i)
        return PVAl
    
    def findPVfirstByPMT(self):
        PVAf = self.findPVlastByPMT()
        return PVAf * (1+self.i)
    
    def findPMTbyPV(self):
        pmt = self.pv * (self.i / (1 - ((1+self.i)**-self.n)))
        return pmt
    
    def findPMTByFV(self):
        pmt = self.fv * (self.i / (((1+self.i)**self.n) - 1))
        return pmt

class calculateN(calculateFun):
    def NByFVPV(self):
        n = (math.log(self.fv/self.pv))/(math.log(1+self.i))
        return n

    def NByPMTandFV(self):
        n = (math.log(((self.fv*self.i)/self.pmt)+1))/(math.log(1+self.i))
        return n
    
    def NByPMTandPV(self):
        top = (math.log(1 - ((self.pv*self.i)/self.pmt)))
        down = (math.log(1+self.i))
        return -top / down
    
class findI(calculateFun): #this is not correct, lt still not work
    def findIByPMT(self):
        return self.pmt * ((((1+I)**self.n) - 1) / I)
        
    def findIByPVFV(self):
        I = ((self.fv/self.pv)**(1/self.n)) - 1
        return I
    
    def findIByPMTandFVlast(self): 
        low = 0.0001
        high = 1.00
        for i in range(100):
            I = (low + high) / 2
            if I == 0:
                continue
            guess = self.findIByPMT()
            if guess > self.fv:
                high = I
            else:
                low = I
        I = I * 100
        return I
    
    def findIByPMTandFVfirst(self):
        low = 0.0001
        high = 1.00
        for i in range(100):
            I = (low + high) / 2
            if I == 0:
                continue
            guess = self.findIByPMT() * (1+I)
            if guess > self.fv:
                high = I
            else:
                low = I
        I = I * 100
        return I
    
class taxcalculate:
    def calculate_tax(self,datavalue):
        return datavalue * 0.07

tax = taxcalculate()
calculate = calculateFun(FV=1000,I=5,N=4,PMT=2500,PV=500)
data = calculate.calculateFV()
MYlist.append(data)
data = calculate.calculatePV()
MYlist.append(data)
for i in range(len(MYlist)):
    print(f"ได้เท่ากับ{MYlist[i]:.2f}")
print(f"หลังคำนวณภาษีFVเท่ากับ: {tax.calculate_tax(calculate.calculateFV()):.2f}")